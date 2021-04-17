def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: ", int(followers))


# Call function with parameters assigned as above
profile_info("sammyshark", 945)

# Call function with keyword arguments
profile_info(username="AlexAnglerfish", followers=342)


def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))


# Call function with parameters assigned as above
profile_info("sammyshark", 945)

# Call function with keyword arguments
profile_info(username="AlexAnglerfish", followers=342)


def profile_info(username, followers=1):
    print("Username: " + username)
    print("Followers: " + str(followers))

profile_info(username="JOctopus")
profile_info(username="sammyshark", followers=945)