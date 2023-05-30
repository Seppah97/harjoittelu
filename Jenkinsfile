pipeline {
    agent any

    parameters{
        choice(name: 'Vaihtoehdot', choices: ['Yksi', 'Kaksi', 'Kolme'], description: 'Tämä on vaihtoehtojen testi')
        string(name: 'Nimi', defaultValue: 'Vakionimi', description: 'Aseta tähän nimi')
        stashedFile 'testi.txt'
        booleanParam(name: 'runDeployment', defaultValue: false, description: 'Toggle this to execute deployment stage')
        //file(name: 'testi.txt', description: 'Testausta')
    }

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        DB_ENGINE = 'sqlite'
        SECRET_INPUT = credentials('testi_secret')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5'))
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
                    
                    if (params.runDeployment == true) {
                        //unstash 'testi.txt'
                        sh "cat $workspace/testi.txt"
                       
                        archiveArtifacts artifacts: 'testi.txt'
                    }

                    else {
                        sh 'echo This is a test'
                    }
                    

            

                
                }

                
                
                //input('Tämä on testi-inputti')
            }
        }

        stage('Testing') {
            steps {
                sh "cat $workspace/testi.txt"
            }
            
        }
    }
    
    post {
        
        always{
            echo 'Tämä on päättynyt'
            sh "rm -rf $workspace/testi.txt"
        }
        
    }
}