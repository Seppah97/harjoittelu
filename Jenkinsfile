pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

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