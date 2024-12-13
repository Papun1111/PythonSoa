import statistics


responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]


frequencyList = [responses.count(rating) for rating in range(1, 6)]


minRating = min(responses)
maxRating = max(responses)
rangeRating = maxRating - minRating
meanRating = statistics.mean(responses)
medianRating = statistics.median(responses)
modeRating = statistics.mode(responses)
varianceRating = statistics.variance(responses)
stdDevRating = statistics.stdev(responses)

print("Frequencies of ratings (1 to 5):", frequencyList)
print("Minimum Rating:", minRating)
print("Maximum Rating:", maxRating)
print("Range:", rangeRating)
print("Mean (Average) Rating:", meanRating)
print("Median Rating:", medianRating)
print("Mode (Most Frequent) Rating:", modeRating)
print("Variance:", varianceRating)
print("Standard Deviation:", stdDevRating)
