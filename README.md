# delete-similar-images
This is a script that takes in a path to a folder of images and a similarity threshold then deletes images in that folder that are over that threshold.

The script will prompt you for a path to the folder and a similarity threshold. The similarity threshold should be a number between 0 and 1 with 1 being 
identical and 0 being completely distinct images.

In testing, it catches small edits pretty well but struggles to find crops.
