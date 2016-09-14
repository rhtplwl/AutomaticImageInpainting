srcFiles = dir('C:\Users\Rohit\Documents\MATLAB\ImageInpaintingCode\Testdata\DamagedData\*.jpg');  % the folder in which ur images exists
for i = 1 : length(srcFiles)
    filename = strcat('C:\Users\Rohit\Documents\MATLAB\ImageInpaintingCode\Testdata\DamagedData\',srcFiles(i).name);
    images = imread(filename);
    %figure,imshow(images);
    grayImages = rgb2gray(images);
    %figure,imshow(grayImages);
    noise = imnoise(grayImages,'salt & pepper', 0.02);
    %figure,imshow(noise);
    FCM = medfilt2(noise);
    %figure,imshow(FCM);
    defect = imabsdiff(grayImages,FCM);
    %figure,imshow(defect);
    mask = im2bw(defect, 0.20);
    %figure,imshow(mask);
   figure, subplot(1,2,1), imshow(images)
    subplot(1,2,2), imshow(mask)
    img_mask = sprintf('C:\\Users\\Rohit\\Documents\\MATLAB\\ImageInpaintingCode\\Testdata\\Masks\\image_mask%d.jpg',i);
    imwrite(mask, img_mask);
    
end