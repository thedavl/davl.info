<template>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #D3D3D3, height: 200px">
        <div class="container" style="padding-top: 15px">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav w-100 justify-content-start">
                </ul>
                <ul class="navbar-nav w-100 justify-content-center">
                    <li v-on:click="setPageTitle" class="nav-item active">
                        <router-link
                            :to="{ name: 'home' }"
                            class="nav-text"
                        >Home
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link
                            :to="{ name: 'blog' }"
                            class="nav-text"
                        >Blog
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link
                            :to="{ name: 'projects' }"
                            class="nav-text"
                        >Projects
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link
                            :to="{ name: 'about-me' }"
                            class="nav-text"
                            st
                        >About Me
                        </router-link>
                    </li>
                </ul>
                <ul class="navbar-nav w-100 justify-content-end">
                    <li v-if="isLoggedIn" class="nav-item">
                        <a class="nav-text" href="/accounts/logout/">Logout</a>
                    </li>
                    <li v-else class="nav-item">
                        <a class="nav-text" href="/accounts/login/">Login</a>
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
        color: lightgray;
    }

    .navbar-name {
        font-weight: bold;
        font-size: 130%;
        color: BLACK
    }

    .navbar-name:hover {
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

    .nav-item {
        margin: 2px;
    }

    .nav-text {
        margin: 10px;
        color: BLACK
    }
</style>