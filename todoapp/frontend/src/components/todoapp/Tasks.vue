<template>
  <div id="container-todoapp" class="col align-self-end position-relative d-flex flex-column" >
    <nav class="navbar navbar-light bg-transparent mt-4">
      <a class="navbar-brand magictime " ref="navTitle"> {{ current.title }} </a>
      <div v-if="current.id !== 1" class="op-menu">
        <button> <i class="fas fa-ellipsis-v"> </i> </button>
      </div>
    </nav>
    <div class="dropdown-divider"></div>

    <div class="flex-grow-1 w-100">
      <ul>
        <li v-for="task in current.tasks" :key="task.id" class="mt-2 mb-5 py-4 px-5 shadow">
            <p class="title">
              <span class="icon mr-3"> 
                <i class="far fa-circle" v-if="!task.state"></i>
                <i class="far fa-check-circle" v-else></i>
            </span>
              {{ task.title }}<small v-if="task.deadline"> by {{ task.deadline }}</small></p>
            <p class="description" >{{ task.description }}</p>
        </li>
      </ul>
    </div>

    <button id="btn-add-task" data-toggle="modal" data-target="#mdlNewTask" class="hvr-wobble-horizontal"> <i class="fas fa-plus-circle hvr-icon"></i> add task </button>

    <ModalNewTask :current="current" @reloadGroup="reloadGroup" />
  </div>
</template>

<style>

  #container-todoapp ul li {
    font-family: 'Montserrat Alternates', sans-serif;
    width: 100% !important;
    color: black;
    cursor: pointer;
    text-align: left;
    padding-top: 10px;
    padding-bottom: 10px;

    -moz-transform: translate(25px, 0px);
    -webkit-transform: translate(25px, 0px);
    -o-transform: translate(25px, 0px);
    -ms-transform: translate(25px, 0px);
    transform: translate(25px, 0px);

    border-right: 3px solid red;
  }

  #container-todoapp ul {
    height: 670px !important;
    overflow-y: scroll !important;
    overflow-x: hidden;
    box-sizing: border-box;
    padding-right: 30px;
  }

  #container-todoapp ul::-webkit-scrollbar-track {
    padding: 2px 0;
    box-shadow: none !important;
    background-color: #D9D9D9;
    border:  none !important;
  }

  #container-todoapp ul::-webkit-scrollbar {
    width: 15px;
  }

  #container-todoapp ul::-webkit-scrollbar-thumb {
    border-radius: 10px;
    box-shadow: none !important;
    background-color: #BF3B5E;
    border:  none !important;
    border-radius: 0px !important;
  }

  #container-todoapp ul li .title {
    font-family: 'Hind Siliguri', sans-serif;
    font-weight: 500;
    font-size: 2rem;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  #container-todoapp ul li .description {
    font-size: 1.4rem;
    font-style: italic;
    font-weight: 400;
  }

  #container-todoapp .navbar .op-menu button i {
    color: #BF3B5E;
    font-size: 2.2rem;
  }

  #container-todoapp .navbar .navbar-brand { 
    color: #8C233F;
    font-family: 'Hind Siliguri', sans-serif;
    font-weight: bold;
    font-size: 3rem;
  }

  #container-todoapp {
    border-bottom-left-radius: 50px;
    background: rgb(255,255,255);
    background: -moz-linear-gradient(214deg, rgba(255,255,255,1) 0%, rgba(251,251,251,1) 33%, rgba(252,252,252,1) 73%, rgba(249,249,249,1) 100%);
    background: -webkit-linear-gradient(214deg, rgba(255,255,255,1) 0%, rgba(251,251,251,1) 33%, rgba(252,252,252,1) 73%, rgba(249,249,249,1) 100%);
    background: linear-gradient(214deg, rgba(255,255,255,1) 0%, rgba(251,251,251,1) 33%, rgba(252,252,252,1) 73%, rgba(249,249,249,1) 100%);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#ffffff",endColorstr="#f9f9f9",GradientType=1);
    height: 110%;
    margin-top: -5%;
  }

  #container-todoapp #btn-add-task {
    position: absolute;
    bottom: -20px;
    right: -100px;

    color: white;

    font-size: 2rem;
    font-family: 'Montserrat Alternates', sans-serif;
    text-transform: uppercase;

    padding: 1rem 3rem;
    border-radius: 15px;
    border-top-right-radius: 0px !important;
    border-bottom-left-radius: 0px !important;

    -webkit-box-shadow: 16px 8px 0px 0px rgba(140,35,63,1) !important;
    -moz-box-shadow: 16px 8px 0px 0px rgba(140,35,63,1) !important;
    box-shadow: 16px 8px 0px 0px rgba(140,35,63,1) !important;

    background: #BF3B5E !important;

    transition: all .15s ease-in-out;
  }

  /* #container-todoapp #btn-add-task:hover {
    background: rgba(140,35,63,1) !important;

    -webkit-box-shadow: 16px -8px 0px 0px #BF3B5E !important;
    -moz-box-shadow: 16px -8px 0px 0px #BF3B5E !important;
    box-shadow: 16px -8px 0px 0px #BF3B5E !important;
  } */

  #container-todoapp #btn-add-task:focus {
    background: rgb(255,255,255);
    
    -webkit-box-shadow: 16px 8px 0px 0px rgba(140,35,63,1) !important;
    -moz-box-shadow: 16px 8px 0px 0px rgba(140,35,63,1) !important;
    box-shadow: 16px 8px 0px 0px rgba(140,35,63,1) !important;
  }
</style>

<script>
import ModalNewTask from './forms/ModalNewTask';

export default {
  name: 'Tasks',
  components: {
    ModalNewTask
  },
  methods: {
    reloadGroup() {
      this.$emit("reloadGroup");
    }
  },
  data() {
    return {
      
    }
  },
  props: {
    msg: String,
    current: Object
  },
  watch: {
    'current': function(val, oldVal){
      let me = this;

      this.$refs.navTitle.classList.add('magictime', 'puffIn');
      setTimeout(function(){
         me.$refs.navTitle.classList.remove('magictime', 'puffIn');
      }, 500);
    }
  },
}
</script>
