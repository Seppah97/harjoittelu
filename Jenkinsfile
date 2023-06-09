pipeline {
    agent any

    parameters{
        choice(name: 'Vaihtoehdot', choices: ['Yksi', 'Kaksi', 'Kolme'], description: 'Tämä on vaihtoehtojen testi')
        string(name: 'Nimi', defaultValue: 'Vakionimi', description: 'Aseta tähän nimi')
        stashedFile 'testi.txt'
        stashedFile 'thumbnail.png'
        booleanParam(name: 'runDeployment', defaultValue: false, description: 'Toggle this to execute deployment stage')
        booleanParam(name: 'runTesting', defaultValue: false, description: 'Toggle this to execute testing stage')
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
        stage('Initial') {
            steps {
                script {
                    echo SECRET_INPUT
                    sh "chmod +x -R ${env.WORKSPACE}"
                    sh './test.sh'

                    //sh 'python3 test_my_application.py'
                    unstash 'testi.txt'
                    unstash 'thumbnail.png'

                    sh 'printenv'

                    

                    def thumbnail = "${env.'thumbnail.png_FILENAME'}"

                    echo "${thumbnail}"

                    if ("${thumbnail}" == "null") {
                        currentBuild.result = 'FAILURE'
                        error "No thumbnail given as parameter"
                    }


                    else if (!("${thumbnail}" =~ /\.(png|jpg)$/)) {
                        currentBuild.result = 'FAILURE'
                        error "Thumbnail is wrong format"
                    }

                }
                
            }
        }

        stage('Deployment') {
            steps {
                script {
                    
                    if (params.runDeployment == true) {
                        
                        sh 'python3 test_my_application.py ' + "$workspace/thumbnail.png"
                    }

                    else {
                        sh 'echo Tämä stage on ohitettu'
                    }
                    

            

                
                }

                
                
                //input('Tämä on testi-inputti')
            }
        }

        stage('Testing') {
            steps {
                script{

                    catchError(message: 'This stage failed for some reason. Please check that everything works.', buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {

                        if (params.runTesting == true) {

                            sh "cat $workspace/t.txt"
                            echo 'Tämä vaihe suoritettiin'
                        }

                        else {
                            echo 'Tätä vaihetta ei suoriteta'
                        }
                    }
                    

                    
                }
                
            }
            
        }

        stage('More testing') {
            steps{
                script{
                    echo 'This prints out, even if previous stage fails.'
                }
            }
        }
    }
    
    post {
        
        always{
            echo 'Tämä on päättynyt'
            //sh "rm -rf $workspace/testi.txt"
        }
        
    }
}