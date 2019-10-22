<template>
    <div>
        <div class="flex-container">
            <div class="project-container">
                <h2>Auto-Sorting Drawer</h2>
                <br>
                <p>
                    As a final project for my high school senior year Design/Tech class, i designed an efficient
                    way to store &#38; retrieve small parts, inspired by the 
                    messy drawers of parts resulting from my 3D printing hobby.</p>
                <p><strong>The design is based on the following goal:</strong></p>

                <p><strong>Create an organizing system that allows for the storage of large quantities of largely 
                    unique parts</strong></p>

                <p> The resulting design is an organizer with LEDs on each drawer, and an accompanying 
                    catalog system. Users enter the name of the item they're storing, and the system lights up 
                    the LED to a drawer to keep the item in. Whenever retrieving an item, the syste, asks for the 
                    item's name and lights up the LED to the location of the item</p>
                
                <p> I fully build one a first prototype of this design, with a fully working cataloging system 
                    written in python onto a Raspberry Pi, with the first row of drawers wired up on the organizer.</p>
                
                <img class="image-container" style="margin-top:11px" v-bind:src="backDrawerWiring">
                <p class="image-text-container">The wiring on the back of the organizer</p>

            </div>
            <div class="project-container">
                <h2>Features and Specifications</h2>
                <ul>
                    <li>Coded in Python</li>
                    <li>The cataloguing system is handled by a Raspberry Pi</li>
                    <li>Ability to store large amounts of traditionally hard-to-catagorize items efficiently</li>
                    
                </ul>
                <img class="image-container" v-bind:src="piPinWiring">
                <p class="image-text-container">The diagram of the Raspberry Pi pin wiring</p>
                <img class="image-container" v-bind:src="breadBoardWiring">
                <p class="image-text-container">The wiring on the prototyping breadboards, and Raspberry Pi unit</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ProjectTwoComponent",
    data() {
        return {
            backDrawerWiring: null,
            piPinWiring: null,
            breadBoardWiring: null

        }
    },
    methods: {
        myFunction: function () {	
            this.backDrawerWiring = "https://i.imgur.com/PYejxlx.jpg";
            this.piPinWiring = "https://i.imgur.com/MZPRQ2d.jpg?1";
            this.breadBoardWiring = "https://i.imgur.com/gEqdqg0.jpg";
        }
    },
    created() {
        this.myFunction()
    }
}
</script>

<style scoped>
.flex-container {
  display: flex;
  flex-wrap: wrap;
}
.project-container {
    padding: 15px;
    width: 480px;
    margin: 10px;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.2), 0 0px 20px 0 rgba(0, 0, 0, 0.19);
}
.image-container {
    width: 320px;

}
.image-text-container {
    width: 325px;
    font-size: 13px;
}
</style>