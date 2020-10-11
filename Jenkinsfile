pipeline {
	agent any
	stages {
		stage("Run the code!") {
			steps {
				sh """
					python Game.py
				"""
			} //steps
		} //stage
		stage("Run unit tests") {
			steps {
				sh """
				    pytest
				"""	
			}
		}
	} //stages
} //pipeline
