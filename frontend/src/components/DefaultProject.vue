<template>
    <div>
        <p class="text-container"><strong>Click one of the projects to learn more!</strong></p>
    </div>
</template>

<script>
export default {
    name: "DefaultProjectComponent",
    data() {
        return {

        }
    },
    methods: {
        myFunction: function () {	
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
    margin-top: 50px;
    text-align: center;
}


</style>
