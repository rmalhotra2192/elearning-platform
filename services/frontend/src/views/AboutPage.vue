<template>
  <div class="lg:w-4/5 mx-auto mt-10 mb-4">
    <section class="mb-16 text-gray-800">
      <div class="grid md:grid-cols-2 gap-4">
        <div class="mb-6 md:mb-0">
          <h2 class="text-3xl font-bold mb-6">About</h2>

          <p class="text-gray-500">
            This is where we describe what "Etudier" is all about.
          </p>
        </div>

        <div class="mb-6 md:mb-0">
          <p class="font-bold mb-4">What is Etudier?</p>
          <p class="text-gray-500 mb-12">
            Etudier is a web application for a hypothetical E-learning platform
            called Etudier (french for "to study").The application is developed
            by me (Rishabh Malhotra) as a part of my PMC 250 Program Curriculum
            at Seneca College.
          </p>

          <p class="font-bold mb-4">
            What was the objective behind creating "Etudier"?
          </p>
          <p class="text-gray-500 mb-12">
            The overall objective of creating this project and deploying it end
            to end was to gain a robust understanding about how to build agile
            development and integration pipelines like CI/CD using AWS Developer
            tools like - AWS CodePipeline and AWS CodeBuild.
          </p>

          <p class="font-bold mb-4">
            Is "Etudier" website publically available to view?
          </p>
          <p class="text-gray-500 mb-12">
            Yes, the application is deployed currently on the following url -
            http://mycicdproject.tk
          </p>

          <p class="font-bold mb-4">Is the code available for "Etudier"?</p>
          <p class="text-gray-500 mb-12">
            The code to the project can be accessed at the following github url
            - https://github.com/rmalhotra2192/elearning-platform
          </p>

          <p class="font-bold mb-4">
            What's the technology stack on which "Etudier" is built upon?
          </p>
          <p class="text-gray-500">
            The application is built upon the following Technology stack:
          </p>
          <div class="text-gray-500 mx-4 mb-12">
            <h3 class="text-md text-gray-700 font-bold mt-4 mb-1">Frontend</h3>
            <ul class="mx-5 space-y-1 list-disc list-inside">
              <li>Vue.JS for SPA functionality</li>
              <li>HTML & Tailwind CSS for UI</li>
            </ul>
            <h3 class="text-md text-gray-700 font-bold mt-4 mb-1">Backend</h3>
            <ul class="mx-5 space-y-1 list-disc list-inside">
              <li>Python</li>
              <li>FastAPI</li>
            </ul>
            <h3 class="text-md text-gray-700 font-bold mt-4 mb-1">Database</h3>
            <ul class="mx-5 space-y-1 list-disc list-inside">
              <li>AWS RDS Powered PostgreSQL for Datapersistence</li>
            </ul>
            <h3 class="text-md text-gray-700 font-bold mt-4 mb-1">
              Source Version Control
            </h3>
            <ul class="mx-5 space-y-1 list-disc list-inside">
              <li>Github</li>
            </ul>
            <h3 class="text-md text-gray-700 font-bold mt-4 mb-1">
              Environment Handling
            </h3>
            <ul class="mx-5 space-y-1 list-disc list-inside">
              <li>Docker Containers</li>
            </ul>
            <h3 class="text-md text-gray-700 font-bold mt-4 mb-1">
              Deployment
            </h3>
            <ul class="mx-5 space-y-1 list-disc list-inside">
              <li>
                AWS CodePipeline for orchestrating the complete build and
                deployment process
              </li>
              <li>AWS CodeBuild for building Docker Container images</li>
              <li>AWS ECR for storing docker container images</li>
              <li>
                AWS Cloud Formation for creating and managing Infrastructure as
                Code
              </li>
              <li>
                AWS ECS Cluster for deploying the application on the Fargate
                instances (serverless).
              </li>
            </ul>
          </div>

          <p class="font-bold mb-4">
            Can you explain the project architecture in an end-to-end fashion?
          </p>
          <p class="text-gray-500 mb-12">
            The project is powered using AWS ECS cluster that is automatically
            deployed using CI/CD pipeline. The CI/CD pipeline is built using the
            AWS CodePipeline, AWS CodeBuild and AWS CloudFormation Services and
            is triggered when changes are detected in source code repository
            i.e. github repository. The architecture of the application is
            depicted in the below given diagram.
            <img
              class="my-10"
              src="https://i.postimg.cc/GtV6BYnb/Docker-Environment-2.png"
            />
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped></style>
