package com.cxc.jigsaw_solver;

import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import nu.pattern.OpenCV;

@SpringBootApplication
public class JigsawSolverApplication {

	public static void main(String[] args) {
		SpringApplication.run(JigsawSolverApplication.class, args);
		OpenCV.loadShared();
	}

	public static Mat loadImage(String imagePath) {
		Imgcodecs imageCodecs = new Imgcodecs();
		return Imgcodecs.imread(imagePath);
	}

	public static void saveImage(Mat imageMatrix, String targetPath) {
		Imgcodecs imgcodecs = new Imgcodecs();
		Imgcodecs.imwrite(targetPath, imageMatrix);
	}
}
