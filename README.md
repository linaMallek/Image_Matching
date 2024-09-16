This project includes two main functionalities:

1-Image Block Matching: Uses the Mean Squared Error (MSE) method to find and highlight matching blocks between two images.
2-Image Difference Detection: Identifies and highlights differences between two images.

The GUI, built with Pygame, provides an interactive menu for users to access these functionalities.

## Key Functions
1- recherche_block:
Purpose: Finds and highlights 16x16 pixel blocks in the target image that match blocks from the reference image using MSE.
Method: Compares blocks with their surrounding blocks to find the best match.

2-recherche_decho:

Purpose: Detects and highlights differences between two images by matching blocks and calculating residuals.
Method: Uses a block matching approach with dichotomous search for improved accuracy.
