<template>
    <div id="container-todolist" class="col-3 h-100 d-flex flex-column">
        <h3> task groups </h3>
        <button id="btn-add-group" @click="openModalAdd" class="py-3 px-5 rounded-pill shadow hvr-ripple-out"> <i class="fas fa-folder-plus"></i> New Group</button>
        <div class="flex-grow-1 w-100">
            <ul v-if="taskgroups.length > 0">
                <TaskGroup v-for="group in taskgroups" :key="group.id" :group="group" @onClicked="taskGroupOnClick" />
            </ul>
        </div>
    </div>
</template>

<style>
    #container-todolist h3 {
        color: white;
        margin-top: 8%;
        font-family: 'Bebas Neue', cursive;
        font-size: 3.2rem;
        letter-spacing: 2px;
    }

    #container-todolist hr {
        border-top: 1px dashed rgba(255,255,255,.3);
        width: 100%;
    }

    #container-todolist #btn-add-group {
        font-size: 2rem;
         font-family: 'Montserrat Alternates', sans-serif;
        text-transform: uppercase;
        
        color: white;
        background: #BF3B5E !important;

        border-top-left-radius: 50px !important;
        border-bottom-left-radius: 50px !important;

        -moz-transform: translate(-50px, 0px);
        -webkit-transform: translate(-50px, 0px);
        -o-transform: translate(-50px, 0px);
        -ms-transform: translate(-50px, 0px);
        transform: translate(-50px, 0px);
    }

    #container-todolist #btn-add-group::before {
        border: none !important;

        border-top-right-radius: 50px !important;
        border-bottom-right-radius: 50px !important;
    }

    #container-todolist #btn-add-group:hover::before{
        border:  #BF3B5E solid 6px !important;
    }

</style>

<script>
import TaskGroup from './TaskGroup';

export default {
  name: 'TasksList',
  components: {
    TaskGroup
  },
  data() {
      return {
          
      }
  },
  props: {
    taskgroups: Array
  },
  methods: {
    taskGroupOnClick(group) {
        this.$emit("onSelectGroup", group);
    },
    openModalAdd() {
        alert('Create new')
    }
  },
}
//eslint-disable-line
</script>
