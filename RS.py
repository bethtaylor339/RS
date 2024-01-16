def get_user_input():
    user_id = input("Please enter your user ID (or 'guest' for general recommendations): ")
    num_recommendations = input("How many recommendations would you like? (Default is 10): ")
    return user_id, num_recommendations

def display_recommendations(recommendations):
    print("Recommended Movies:")
    for idx, movie in enumerate(recommendations, 1):
        print(f"{idx}. {movie['title']} - Reason: {movie['reason']}")

def main():
    user_id, num_recommendations = get_user_input()
    # Call the hybrid recommendation function
    # recommendations = get_hybrid_recommendations(user_id, num_recommendations)
    
    # Display the recommendations
    display_recommendations(recommendations)

if __name__ == "__main__":
    main()
