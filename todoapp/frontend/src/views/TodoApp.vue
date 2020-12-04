<template>
  <div class="row d-flex justify-content-md-center align-items-center h100-vh m-0">
    <div id="container-card" class="col-8">
      <div class="row h-100">
        <TasksList :taskgroups="taskgroups" @onSelectGroup="selectGroup" />
        <Tasks :current="currentGroup" @reloadGroup="loadGroups" />
      </div>
    </div>
  </div>
</template>

<style>
  #container-card {
    height: 700px;
    border-radius: 5px;
    background: rgb(13,13,13);
    background: -moz-linear-gradient(20deg, rgba(13,13,13,1) 0%, rgba(83,25,41,1) 55%, rgba(140,35,63,1) 100%);
    background: -webkit-linear-gradient(20deg, rgba(13,13,13,1) 0%, rgba(83,25,41,1) 55%, rgba(140,35,63,1) 100%);
    background: linear-gradient(20deg, rgba(13,13,13,1) 0%, rgba(83,25,41,1) 55%, rgba(140,35,63,1) 100%);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#0d0d0d",endColorstr="#8c233f",GradientType=1);
    -webkit-box-shadow: -35px 35px 77px -49px rgba(0,0,0,0.75);
    -moz-box-shadow: -35px 35px 77px -49px rgba(0,0,0,0.75);
    box-shadow: -35px 35px 77px -49px rgba(0,0,0,0.75);
  }
</style>

<script>
import TasksList from '@/components/todoapp/TasksList.vue'
import Tasks from '@/components/todoapp/Tasks.vue'

import clientAxio from '@/tools/axios'

export default {
  name: 'TodoApp',
  data() {
    return {
      taskgroups: [],
      currentGroup: {}
    }
  },
  components: {
    TasksList,
    Tasks
  }, 
  methods: {
    selectGroup(taskGroup) {
      const groupId = taskGroup.id;

      this.taskgroups = this.taskgroups.map( (group, index) => ({ 
        ...group,
        show: group.id === groupId
      }));

      this.currentGroup = taskGroup;
    },
    loadGroups() {
      let me = this;

      clientAxio.get('groups/?format=json').then(response => {

        const check_index = (this.currentGroup.id === undefined)? 1 : this.currentGroup.id;

        const result = response.data;
        this.taskgroups = result.map( (group, index) => ({ 
          ...group,
          show: group.id === check_index
        }));

        for (var i = 0; i < this.taskgroups.length; i++){
          if (this.taskgroups[i].id == check_index){
            this.currentGroup = this.taskgroups[i];
          }
        }

        console.log('load')
      });
    }
  },
  mounted() {
    this.loadGroups();
  },
}
</script>
