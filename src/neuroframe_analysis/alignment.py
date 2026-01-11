# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np
import matplotlib.pyplot as plt



# ================================================================
# 1. Section: Obtaining the Mouse Alignment
# ================================================================
def get_alignment(ct: np.ndarray, mri: np.ndarray, brain_mask: np.ndarray) -> float:
    # 1. remove the brain in the mri with the brain mask
    mri = np.where(brain_mask == 0, mri, 0)

    plt.figure()
    plt.imshow(mri[:,:,50])
    plt.show(block=False)

    plt.figure()
    plt.imshow(ct[:,:,50])
    plt.show(block=True)
    # 2. threshold both
    # 3. Count the number of voxels in the smallest mask
    # 4. Compute how many voxels overlap between mri and ct mask
    # 5. Get a percentage of overlap regarding the smallest mask
    # 6. The better the overlap the better the alignment
    return 0.0
