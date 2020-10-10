pipeline {
	agent any
	stages {
		stage("Run the code!") {
			steps {
				sh """
					python Jenkinsfile.py
				"""
			} //steps
		} //stage
	} //stages
} //pipeline
