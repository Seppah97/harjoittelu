pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'echo Tämä on testivaihe'
            }
        }
    }
    
    post {
        
        always{
            echo 'Tämä on päättynyt'
        }
        
    }
}