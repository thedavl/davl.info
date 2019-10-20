<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            
            <div v-on:click="setPageTitle">
                <router-link
                    :to="{ name: 'home' }"
                    class="navbar-brand"
                    
                >David Lee
                </router-link>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ml-auto">
                <li v-on:click="setPageTitle" class="nav-item active">
                    <router-link
                        :to="{ name: 'home' }"
                        class="btn btn-sm btn-success"
                    >Home
                    </router-link>
                </li>
                <li class="nav-item mx-1">
                    <router-link
                        :to="{ name: 'blog' }"
                        class="btn btn-sm btn-info"
                    >Blog
                    </router-link>
                </li>
                <li class="nav-item mr-1">
                    <router-link
                        :to="{ name: 'projects' }"
                        class="btn btn-sm btn-primary"
                    >Projects
                    </router-link>
                </li>
                <li class="nav-item mr-1">
                    <router-link
                        :to="{ name: 'about-me' }"
                        class="btn btn-sm btn btn-dark"
                    >About Me
                    </router-link>
                </li>
                <li v-if="isLoggedIn" class="nav-item">
                    <a class="btn btn-sm btn-outline-danger" href="/accounts/logout/">Logout</a>
                </li>
                <li v-else class="nav-item">
                    <a class="btn btn-sm btn-outline-danger" href="/accounts/login/">Login</a>
                </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
    name: "NavBarComponent",
    data() {
        return {
            currentUser: null
        };
    },
    computed: {
        isLoggedIn() {
            return this.currentUser !== "";
        }
    },
    methods: {
        setPageTitle() {
            document.title = "David's Portfolio";
        },
        setCurrentUser() {
            let endpoint = `api/user/`;
            apiService(endpoint).then(data => {
                if (data) {
                    this.currentUser = data.username;
                } else {
                this.setPageTitle("username error");
                }
            });
        }
    },
    created() {
        this.setCurrentUser();
  }
}
</script>

<style>
    .my-navbar {
        border-bottom: 1px solid #DDD;
    }

    .navbar-brand {
        font-weight: bold;
        font-size: 130%;

    }

    .navbar-brand:hover {
        color: #DC3545 !important;
    }

    .btn-dark {
        background-color: rgb(170, 0, 204);
        color: white;
        border-color: rgb(170, 0, 204);
    }

    .btn-dark:hover,
    .btn-dark:active    {
        background-color: rgb(126, 0, 151);
        color: #FFF;
        border-color: rgb(126, 0, 151);
    }
</style>