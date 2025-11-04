# Image Search
# On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

# Given an array of image names and a search term, return an array of image names containing the search term.

# Ignore the case when matching the search terms.
# Return the images in the same order they appear in the input array.

# def image_search(images: list[str], term: str) -> list[str]:
#     search_results = []
#     for image in images:
#         if term.lower() in image.lower():
#             search_results.append(image)
#     return search_results

def image_search(images: list[str], term: str) -> list[str]:
    return [image for image in images if term.lower() in image.lower()]

# Tests
# Test 12345 should return ["dog.png"].
print(image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog"))
# Test 2 should return ["Sunset.jpg", "sunflower.jpeg"].
print(image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"))
# Test 3 should return ["Moon.png", "stars.png"].
print(image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG"))
# Test 4 should return ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"].
print(image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat"))