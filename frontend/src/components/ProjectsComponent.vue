<template>
    <div id="link-center">
        <div class="fade-container">
            Noteable Projects
            <div class="flex-container">
                <div class="project-card">
                    <img class="project-card-image" src="@/assets/codebrain.png" />
                    <div class="project-card-title-background">
                        <p class="project-card-title">
                            CodeBrain
                        </p>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-card-title-background">
                        <p class="project-card-title">
                            FitFriends
                        </p>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-card-title-background">
                        <p class="project-card-title">
                            LinkOut
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ProjectsComponent"
}
</script>

<style scoped>
.project-card {
    position: relative;
    border: 1px solid black;
    width: 300px;
    height: 300px;
    margin: 10px 10px 0 10px;
    border-radius: 5px;
}
.project-card:hover {
    cursor: pointer;
}
.project-card:hover img {
    filter: brightness(50%);
}
.project-card-title {
    position: absolute;
    top: 50%;
    left: 50%;
    font-size: 40px;
    transform: translate(-50%, -50%);
}
.project-card-title-background {
    height: 80px;
    width: 299px;
    border-radius: 0 0 5px 5px;
    background-color: white;
    position: absolute;
    top: 86.6%;
    left: 50%;
    transform: translate(-50%, -50%);
}
.project-card-image {
    border-radius: 5px;
    object-fit: cover;
    width: 100%;
    height: 298px;
}
</style>