
import cv2
import os

original_mask_path = "/home/usama/diffBIR_results/LUV__low_res_Meanshift_Bandwidth_8/demo77/demo77_10.jpg"
mask_path = "/home/usama/Usama_ahmad_/new_folder/pcd-filter-tugas1/filter2.png"
original_mask_path = cv2.imread(original_mask_path)
mask_path = cv2.imread(mask_path)
result = cv2.addWeighted(original_mask_path, 0.5, mask_path, 0.5, 0)
cv2.imwrite("Overlay_mask.png", result)

