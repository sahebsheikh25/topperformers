def get_top_performers(gradebook, threshold):

    # Store unique top performers
    top_performers = set()

    # Calculate average for each student
    for student, scores in gradebook.items():

        average = sum(scores) / len(scores)

        # Check threshold
        if average >= threshold:
            top_performers.add(student)

    # Return sorted list
    return sorted(top_performers)


# Student gradebook
gradebook = {
    "Ana": [80, 90, 85],
    "Rohit": [60, 70, 65],
    "Saheb": [95, 90, 100],
    "Ruchi": [75, 80, 85]
}

# Set minimum average score
threshold = 80

# Function call
result = get_top_performers(gradebook, threshold)

# Display result
print("Top Performers:", result)