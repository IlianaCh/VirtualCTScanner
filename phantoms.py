import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import disk, rectangle, rectangle_perimeter, circle_perimeter
from phantominator import shepp_logan


from skimage.draw import disk

def create_circular_phantom(image_size, color_factor, size_factor):
    """
    Creates the first original phantom using a function
    
    :param image_size: Size of the image (height, width)
    :param color_factor: Adjusts the color of the circles. The default value is 1
    :param size_factor: Adjust the size of the circles. The default value is 1
    :return: A 2D numpy array representing the phantom with all the shapes in our requirenments.
    """
    # Initialize the image with zeros
    phantom = np.zeros(image_size)
    
    # Draw the outer circle (the body)
    rr, cc = disk((image_size[0]//2, image_size[1]//2), image_size[0]//2 - 10)
    phantom[rr, cc] = 0.4 # Colring: Light gray for the outer circle

    # List of centers and radii for the circles
    # Can be edited to change the location and sizes of shapes if you need to
    circles = [
        ((image_size[0]//2, image_size[1]//2), 20 * size_factor),  # Center circle
        ((image_size[0]//2 + 50, image_size[1]//2), 15 * size_factor),  # Smaller circle below
        ((image_size[0]//2 - 50, image_size[1]//2 - 10), 5 * size_factor),   # Tiny circle above
        ((image_size[0]//2 + 10, image_size[1]//2 - 60), 10 * size_factor),  # Circle to the left
    ]
    
    # Drawing the circles and their outlines (I put outlines to make it look more like the images provided)
    for (y, x), radius in circles:
        rr, cc = disk((y, x), radius)
        phantom[rr, cc] = 0.7 * color_factor # Coloring: Gray shade for the circles

    # Drawing the outline for the outer circle
    rr_perim, cc_perim = circle_perimeter(image_size[0]//2, image_size[1]//2, image_size[0]//2 - 10)
    phantom[rr_perim, cc_perim] = 0  # Black outline for the outer circle

    return phantom



def create_rectangular_phantom(image_size, color_factor, size_factor):
    """
    Creates the second original phantom using a function
    
    :param image_size: Size of the image (height, width)
    :param color_factor: Adjusts the color of the circles. The default value is 1
    :param size_factor: Adjust the size of the circles. The default value is 1
    :return: A 2D numpy array representing the phantom with the rectangular shape.
    """

    phantom = np.zeros(image_size)
    
    rr, cc = disk((image_size[0]//2, image_size[1]//2), image_size[0]//2 - 10)
    phantom[rr, cc] = 0.4  # Coloring

    # Calculating the start coordinates for a rectangle in the middle
    rect_height, rect_width = 40 * size_factor, 80 * size_factor
    start = (image_size[0]//2 - rect_height//2, image_size[1]//2 - rect_width//2)

    # Add rectangle (the structure)
    rr, cc = rectangle(start, extent=(rect_height, rect_width), shape=image_size)
    phantom[rr, cc] = 0.7 * color_factor # Coloring: Dark grey

    # rr_perim, cc_perim = rectangle_perimeter(start, extent=(rect_height, rect_width), shape=image_size)
    # phantom[rr_perim, cc_perim] = 0  #Black outline for the rectangle

    rr_perim, cc_perim = circle_perimeter(image_size[0]//2, image_size[1]//2, image_size[0]//2 - 10)
    phantom[rr_perim, cc_perim] = 0  # Black outline for the outer circle
    
    return phantom



def create_head_phantom(image_size):
    """
    Creates the first original phantom using a function
    
    :param image_size: Size of the image (height, width)
    :return: A 2D numpy array representing the phantom with all the shapes in our requirenments.
    """
    # Initialize the image with zeros
    phantom = np.zeros(image_size)
    
    phantom = shepp_logan(image_size)

    return phantom



# # TESTING circular phantom only
# image_size = (200, 200)
# circular_phantom_with_outlines = create_circular_phantom(image_size, 1, 1)
# plt.imshow(circular_phantom_with_outlines, cmap='gray')
# plt.title('Circular Phantom with Outlines')
# plt.axis('off')
# plt.show()

# # Plot the rectangular phantom
# image_size = (200, 200)
# rectangular_phantom = create_rectangular_phantom(image_size, 1, 1)
# plt.imshow(rectangular_phantom, cmap='gray')
# plt.title('Rectangular Phantom')
# plt.axis('off')
# plt.show()

# # TESTING circular phantom only
# image_size = (200, 200)
# head_phantom = create_head_phantom(image_size)
# plt.imshow(head_phantom, cmap='gray')
# plt.title('Head Phantom')
# plt.axis('off')
# plt.show()