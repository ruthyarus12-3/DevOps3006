properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/ruthyarus12-3/DevOps3006.git"
    }
    stage("show files"){
        sh "ls -l"
    }
}
