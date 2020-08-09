import os
import json
import numpy as np
import matplotlib.pyplot as plt
import sys
import h5py


vibe_dir = '' # folder containing the json files.
reqd_joints = [38, 43, 44, 45, 46, 47, 48, 40, 37, 33,32,31, 34,35,36, 41, 39, 27,26,25, 28,29,30, 22, 19]
idx = 0
files_order = []
joint_data_final = []
labels_final = []
for num, class_name in enumerate(os.listdir(vibe_dir)):
    for file_name in os.listdir(os.path.join(vibe_dir, class_name)): # add path to the json files here
    #     print(j)
    #     file_name = os.path.join(vibe_dir,j)
        print(file_name)
        with open (file_name, 'r') as f:
            data = json.load(f)
        files_order.append(file_name)
        f.close()
        person_list = list(data.keys())
        if (person_list == []):
            print(file_name)
            continue
        frame_vids = []
        for k in (person_list):
            frame_vids.append(np.array(data[k]['joints3d']).shape[0])
        if (len(person_list) == 1):
            frames = np.array(data[person_list[0]]['frame_ids'])
            joint_data_1 = np.array(data[person_list[0]]['joints3d'])[:,reqd_joints,:]
            joint_data_1 = np.reshape(joint_data_1, (joint_data_1.shape[0],75))
            final_data = np.zeros((300,150))
            final_data[frames,0:75] = joint_data_1[:,:]
            missing_frames = sorted(list(set(np.arange(max(frames)+1)) - set(frames)))
            for mf in missing_frames:
                if len(frames[frames>mf]) != 0 and len(frames[frames<mf]) != 0:
                    e = min(frames[frames>mf])
                    s = max(frames[frames<mf])
                    final_data[mf, 0:75] = final_data[s, 0:75]*((mf - s)/(e-s)) + final_data[e, 0:75]*((e - mf)/(e-s))
        else:
            final_data = np.zeros((300,150))
            person_id = np.argsort(np.array(frame_vids))[-2:][::-1]
            frames = np.array(data[person_list[person_id[0]]]['frame_ids'])
            joint_data_1 = np.array(data[person_list[person_id[0]]]['joints3d'])[:,reqd_joints,:]
            joint_data_1 = np.reshape(joint_data_1, (joint_data_1.shape[0],75))
            final_data[frames, 0:75] = joint_data_1[:,:]
            missing_frames = sorted(list(set(np.arange(max(frames)+1)) - set(frames)))
            for mf in missing_frames:
                if len(frames[frames>mf]) != 0 and len(frames[frames<mf]) != 0:
                    e = min(frames[frames>mf])
                    s = max(frames[frames<mf])
                    final_data[mf, 0:75] = final_data[s, 0:75]*((mf - s)/(e-s)) + final_data[e, 0:75]*((e - mf)/(e-s)) 

            frames = np.array(data[person_list[person_id[1]]]['frame_ids'])
            joint_data_2 = np.array(data[person_list[person_id[1]]]['joints3d'])[:,reqd_joints,:]
            joint_data_2 = np.reshape(joint_data_2, (joint_data_2.shape[0],75))
            final_data[frames, 75:] = joint_data_2[:,:]
            missing_frames = sorted(list(set(np.arange(max(frames)+1)) - set(frames)))
            for mf in missing_frames:
                if len(frames[frames>mf]) != 0 and len(frames[frames<mf]) != 0:
                    e = min(frames[frames>mf])
                    s = max(frames[frames<mf])
                    final_data[mf, 75:] = final_data[s, 75:]*((mf - s)/(e-s)) + final_data[e, 75:]*((e - mf)/(e-s)) 

            # print (final_data.shape)
        joint_data_final.append(final_data)
        labels_final.append(num)

joint_data_final = np.array(joint_data_final)
labels_final = np.array(labels_final)
print (joint_data_final.shape)
print (labels_final.shape)


# file_n = h5py.File('dataset.h5','w')
# file_n.create_dataset('x',data = joint_data_final)
# file_n.create_dataset('y',data = labels_final)
# file_n.close()
# 147 GB 85 GB

os.mkdir('/ssd_scratch/cvit/pranay.gupta/ntu_splits_msg3d/'+str(ss)+'_'+st+'/') # path where weights need to be saved
train_x = np.array(joint_data_final).reshape(-1,300,2,25,3).transpose((0,4,1,3,2))
train_x = train_x[:,:,:,:,:]
np.save('path for the new dataset', train_x)

train_y = np.argmax(labels_final, -1)
np.save('path for the new dataset', train_y)

