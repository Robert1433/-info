<?php
	$language = strtolower($_POST['language']);
	$code = $_POST['code'];
	$random = substr(md5(mt_rand()),0,7);
	$filePath = "temp/". $random. ".".$languages;
	$program = fopen($filePath,"w");
	fwrite($programFile,$code);
	fclose($programFile);

	if($language == 'c'){
		$outputexe = $random . ".exe";
		shell_exec("gcc $filePath -o $outputExe");
		$output = shell_exec(__DIR__."//$outputexe");
		echo $output;
	}


	if($language == 'c++'){
		$outputexe = $random . ".exe";
		shell_exec("g++ $filePath -o $outputExe");
		$output = shell_exec(__DIR__."//$outputexe");
		echo $output;
	}
