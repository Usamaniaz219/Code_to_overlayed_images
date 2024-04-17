# import cv2
# import os

# def overlay_images(original_path, mask_folder, output_folder):
#     # Create output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     mask_images = [f for f in sorted(os.listdir(mask_folder)) if f.endswith('.jpg')]

#     # Process each mask image
#     for mask_image in mask_images:
#         mask_path = os.path.join(mask_folder, mask_image)
#         output_path = os.path.join(output_folder, f"{mask_image.split('.')[0]}_overlay.jpg")

#         # Read original and mask images using OpenCV
#         original = cv2.imread(original_path)
#         mask = cv2.imread(mask_path)

#         # Ensure both images have the same size
#         original = cv2.resize(original, (mask.shape[1], mask.shape[0]))

#         # Convert mask to RGBA
#         mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

#         # Blend images
#         result = cv2.addWeighted(original, 0.5, mask_rgb, 0.5, 0)

#         # Save the result
#         cv2.imwrite(output_path, result)

#         print(f"Overlay image saved: {output_path}")

# if __name__ == "__main__":
#     original_image_path = "/home/usama/diffBIR_results/LUV_Meanshift_Bandwidth_11_8/data11/data11/demo178_69.jpg"
#     mask_images_folder = "/home/usama/Fill_hole_inside_mask_images/demo178_69_output16/"
#     output_folder = "/home/usama/Fill_hole_inside_mask_images/demo178_69_output16_overlays"

#     overlay_images(original_image_path, mask_images_folder, output_folder)


import cv2
import os

original_mask_path = "/home/usama/diffBIR_results/LUV__low_res_Meanshift_Bandwidth_8/demo77/demo77_10.jpg"
mask_path = "/home/usama/Usama_ahmad_/new_folder/pcd-filter-tugas1/filter2.png"
original_mask_path = cv2.imread(original_mask_path)
mask_path = cv2.imread(mask_path)
result = cv2.addWeighted(original_mask_path, 0.5, mask_path, 0.5, 0)
cv2.imwrite("Overlay_mask.png", result)

