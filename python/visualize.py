import cv2
import numpy as np
import json
from glob import glob
import argparse

def plotEyeGaze(img, eyeGaze,eye_c):

	look_vec_left = np.array([eval(s) for s in eyeGaze])[0]
	look_vec_left[0] = -look_vec_left[0]
	look_vec_left[1] = -look_vec_left[1]

	cv2.line(img, tuple(eye_c), tuple(eye_c+(np.array(look_vec_left[:2])*80).astype(int)), (0,0,0), 3)
	cv2.line(img, tuple(eye_c), tuple(eye_c+(np.array(look_vec_left[:2])*80).astype(int)), (0,255,255), 2)

def plotEyeLM(img,ldmks_eyelid, ldmks_pupil, ldmks_iris):

	# Draw black background points and lines
	for ldmk in np.vstack([ldmks_eyelid, ldmks_pupil, ldmks_iris[::2]]):
	    cv2.circle(img, (int(ldmk[0]), int(ldmk[1])), 3, (0,0,0),-1)
	cv2.polylines(img, np.array([ldmks_eyelid[:,:2]], int), True, (0,0,0), 2)
	cv2.polylines(img, np.array([ldmks_pupil[:,:2]], int), True, (0,0,0), 2)
	cv2.polylines(img, np.array([ldmks_iris[:,:2]], int), True, (0,0,0), 2)

	# Draw green foreground points and lines
	for ldmk in np.vstack([ldmks_eyelid,ldmks_pupil, ldmks_iris[::2]]):
	    cv2.circle(img, (int(ldmk[0]), int(ldmk[1])), 2, (0,255,0),-1)
	cv2.polylines(img, np.array([ldmks_eyelid[:,:2]], int), True, (0,255,0), 1)
	cv2.polylines(img, np.array([ldmks_pupil[:,:2]], int), True, (0,255,0), 1)
	cv2.polylines(img, np.array([ldmks_iris[:,:2]], int), True, (0,255,255), 1)

def plotGT(folder_path):
	json_fns = glob(folder_path+"*.json")

	for json_fn in json_fns:

		img = cv2.imread("%s.png"%json_fn[:-5])
		data_file = open(json_fn)
		data = json.load(data_file)

		def process_json_list(json_list):
			ldmks = [eval(s) for s in json_list]
			return np.array([(x, img.shape[0]-y, z) for (x,y,z) in ldmks])

		# Read LandMarks
		ldmks_eyelid_left= process_json_list( data['eyelid_left'])
		ldmks_pupil_left = process_json_list( data['pupil_left'])
		ldmks_iris_left = process_json_list( data['iris_left'])

		ldmks_eyelid_right= process_json_list( data['eyelid_right'])
		ldmks_pupil_right = process_json_list( data['pupil_right'])
		ldmks_iris_right = process_json_list( data['iris_right'])

		# Plot Eye LandMarks
		plotEyeLM(img, ldmks_eyelid_left, ldmks_pupil_left, ldmks_iris_left)
		plotEyeLM(img, ldmks_eyelid_right, ldmks_pupil_right, ldmks_iris_right)

		# Estimate the center of the eye
		eyeLeftCenter = np.mean(ldmks_iris_left[:, :2], axis=0).astype(int)
		eyeRightCenter = np.mean(ldmks_iris_right[:, :2], axis=0).astype(int)

		# Plot Gaze
		plotEyeGaze(img, data['look_vec_left'], eyeLeftCenter)
		plotEyeGaze(img, data['look_vec_right'], eyeRightCenter)

		cv2.imshow("Synthetic Image", img)
		cv2.waitKey(0)

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Plot Eyelid GT')
	parser.add_argument('--folder', metavar='path', required=False,
						help='the path to Ground-Truth folder',
						default = 'test/')
	args = parser.parse_args()
	# Main call
	plotGT(args.folder)

