<template>
    <div>
        <img class="arrow-container" v-bind:src="arrow">
        <p class="text-container"><strong>Click one of the projects to learn more!</strong></p>
    </div>
</template>

<script>
export default {
    name: "DefaultProjectComponent",
    data() {
        return {
            arrow: null

        }
    },
    methods: {
        myFunction: function () {	
            this.arrow = "https://i.imgur.com/cIFoOKq.png";
        }
    },
    created() {
        this.myFunction()
    }
}
</script>

<style>
.flex-container {
  display: flex;
  justify-content: center;
  align-items: center, stretch;
}
.text-container {
    margin-top: 5px;
}

.arrow-container {
    margin-top: -10px;
    width: 140px;
    height: 70px;
}


</style>
