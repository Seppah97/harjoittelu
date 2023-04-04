pipeline {
    agent any

    parameters{
        choice(name: 'Vaihtoehdot', choices: ['Yksi', 'Kaksi', 'Kolme'], description: 'Tämä on vaihtoehtojen testi')
        string(name: 'Nimi', defaultValue: 'Vakionimi', description: 'Aseta tähän nimi')
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
            }
        }

        stage('Deployment') {
            steps {
                script {
                    sh 'echo Tämä on julkaisu'
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