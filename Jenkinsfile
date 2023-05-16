pipeline {
    agent any

    parameters{
        choice(name: 'Vaihtoehdot', choices: ['Yksi', 'Kaksi', 'Kolme'], description: 'Tämä on vaihtoehtojen testi')
        string(name: 'Nimi', defaultValue: 'Vakionimi', description: 'Aseta tähän nimi')
        file(name: 'testaus')
    }

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        DB_ENGINE = 'sqlite'
        SECRET_INPUT = credentials('testi_secret')
    }

    stages {
        stage('Test') {
            steps {
                echo SECRET_INPUT
                sh "chmod +x -R ${env.WORKSPACE}"
                sh './test.sh'

                sh 'python3 test_my_application.py'
            }
        }

        stage('Deployment') {
            steps {
                script {
                     archiveArtifacts artifacts: params.testaus
                
                }
                
                input('Tämä on testi-inputti')
            }
        }
    }
    
    post {
        
        always{
            echo 'Tämä on päättynyt'
        }
        
    }
}