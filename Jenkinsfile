pipeline {
	agent any
	stages {
		stage("Run the code!") {
			steps {
				sh """
					python3 Game.py
				"""
			} //steps
		} //stage
		stage("Run unit tests") {
			steps {
				sh """
				    pytest3 -m pytest
				"""	
			}
		}
	} //stages
} //pipeline
