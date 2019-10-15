<template>
    <div>
        <br>
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto">
                <li class="nav-item">
                    <button
                        type="button"
                        v-on:click="toggleThisWebsite"
                        class="btn btn-sm btn-outline-info ml-1"
                        data-toggle="button"
                        autocomplete="off"
                    >This Website
                    </button>
                    <button
                        type="button"
                        v-on:click="toggleProjectTwo"
                        class="btn btn-sm btn-outline-info ml-1"
                        data-toggle="button"
                        aria-pressed="true"
                        autocomplete="off"
                    >Auto-Sort Drawer
                    </button>
                </li>
                </ul>
            </div>
        </nav>
        <div align="center" style="margin-top:10px">
            <ThisWebsiteComponent v-if="displayThisSite" />
            <ProjectTwoComponent v-else-if="display2" />
            <DefaultProjectComponent v-else />
        </div>
    </div>
</template>

<script>
import ThisWebsiteComponent from "@/components/ThisWebsite.vue"
import ProjectTwoComponent from "@/components/ProjectTwo.vue"
import DefaultProjectComponent from "@/components/DefaultProject.vue"

export default {
    name: "ProjectsNavbarComponent",
    components: {
        ThisWebsiteComponent,
        ProjectTwoComponent,
        DefaultProjectComponent
    },
    data() {
        return {
            // research using "isActive" vue functionality
            displayThisSite: false,
            display2: false
        }
  
    },
    methods: {
        toggleThisWebsite() {
            this.displayThisSite = !this.displayThisSite;
            this.display2 = false;

        },
        toggleProjectTwo() {
            this.display2 = !this.display2;
            this.displayThisSite = false;
        }
    }
}
</script>
