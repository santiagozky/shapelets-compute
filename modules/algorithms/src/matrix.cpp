// Copyright (c) 2019 Shapelets.io
//
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

#include <algos/internal/libraryInternal.h>
#include <algos/internal/matrixInternal.h>
#include <algos/matrix.h>

#include <stdexcept>

namespace {
constexpr long BATCH_SIZE_SQUARED = 2048;
constexpr long BATCH_SIZE_B = 1024;
constexpr long BATCH_SIZE_A = 8192;
}  // namespace

namespace khiva {
namespace matrix {

void mass(const af::array &q, const af::array &t, af::array &distances) {
    af::array aux, mean, stdev;
    auto qReordered = af::reorder(q, 0, 3, 2, 1);
    auto m = qReordered.dims(0);
    internal::meanStdev(t, aux, m, mean, stdev);
    internal::mass(qReordered, t, aux, mean, stdev, distances);
    distances = af::reorder(distances, 2, 0, 1, 3);
}

void findBestNOccurrences(const af::array &q, const af::array &t, long n, af::array &distances, af::array &indexes) {
    if (n > t.dims(0) - q.dims(0) + 1) {
        throw std::invalid_argument("You cannot retrieve more than (L-m+1) occurrences.");
    }

    if (n < 1) {
        throw std::invalid_argument("You cannot retrieve less than one occurrences.");
    }

    af::array distancesGlobal;

    khiva::matrix::mass(q, t, distancesGlobal);

    af::array sortedDistances;
    af::array sortedIndexes;

    af::sort(sortedDistances, sortedIndexes, distancesGlobal);

    indexes = sortedIndexes(af::seq(n), af::span, af::span);
    distances = sortedDistances(af::seq(n), af::span, af::span);
}

void findBestNMotifs(const af::array &profile, const af::array &index, long m, long n, af::array &motifs,
                     af::array &motifsIndices, af::array &subsequenceIndices, bool selfJoin) {
    internal::findBestN(profile, index, m, n, motifs, motifsIndices, subsequenceIndices, selfJoin, true);
}

void findBestNDiscords(const af::array &profile, const af::array &index, long m, long n, af::array &discords,
                       af::array &discordsIndices, af::array &subsequenceIndices, bool selfJoin) {
    internal::findBestN(profile, index, m, n, discords, discordsIndices, subsequenceIndices, selfJoin, false);
}

void stomp(const af::array &ta, const af::array &tb, long m, af::array &profile, af::array &index) {
    auto batchSizeSquared = library::internal::getValueScaledToMemoryDevice(
        BATCH_SIZE_SQUARED, khiva::library::internal::Complexity::CUADRATIC);
    if (tb.dims(0) > batchSizeSquared) {
        if (ta.dims(0) > batchSizeSquared) {
            // Calculates the distance and index profiles using a double batching strategy. First by the number of query
            // sequences from tb to compare simultaneously; and second, the chunk size of the reference time series ta
            return internal::stomp_batched_two_levels(ta, tb, m, batchSizeSquared, batchSizeSquared, profile, index);
        } else {
            // Calculates the distance and index profiles using a batching strategy by the number of query
            // sequences from tb to compare simultaneously
            return internal::stomp_batched(ta, tb, m, batchSizeSquared, profile, index);
        }
    } else {
        // Doing it in parallel
        return internal::stomp_parallel(ta, tb, m, profile, index);
    }
}

void stomp(const af::array &t, long m, af::array &profile, af::array &index) {
    const auto batchSizeSquared = library::internal::getValueScaledToMemoryDevice(
        BATCH_SIZE_SQUARED, khiva::library::internal::Complexity::CUADRATIC);

    const auto batchSizeB =
        library::internal::getValueScaledToMemoryDevice(BATCH_SIZE_B, khiva::library::internal::Complexity::CUADRATIC);

    const auto batchSizeA =
        library::internal::getValueScaledToMemoryDevice(BATCH_SIZE_A, khiva::library::internal::Complexity::CUADRATIC);
    if (t.dims(0) > batchSizeSquared) {
        // Calculates the distance and index profiles using a double batching strategy. First by the number of query
        // sequences from t to compare simultaneously; and second, the chunk size of the reference time series t
        return internal::stomp_batched_two_levels(t, m, batchSizeB, batchSizeA, profile, index);
    } else {
        // Doing it in parallel
        return internal::stomp_parallel(t, m, profile, index);
    }
}

void matrixProfile(const af::array &tss, long m, af::array &profile, af::array &index) {
    internal::scamp(tss, m, profile, index);
}

void matrixProfile(const af::array &ta, const af::array &tb, long m, af::array &profile, af::array &index) {
    internal::scamp(ta, tb, m, profile, index);
}

void matrixProfileLR(const af::array &tss, long m, af::array &profileLeft, af::array &indexLeft,
                     af::array &profileRight, af::array &indexRight) {
    internal::scampLR(tss, m, profileLeft, indexLeft, profileRight, indexRight);
}

void getChains(const af::array &tss, long m, af::array &chains) { internal::getChains(tss, m, chains); }

}  // namespace matrix
}  // namespace khiva
