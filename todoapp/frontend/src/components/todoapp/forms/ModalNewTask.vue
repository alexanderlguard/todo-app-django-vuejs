<template>
    <div class="modal fade " id="mdlNewTask" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header p-0 py-3">
            <h5 class="modal-title px-4">
              
              <p class="title"><i class="fas fa-edit"></i> What do You want to do?</p>
              <small class="pl-5">this task will save in <strong>{{ current.title }}</strong> </small>
              
            </h5>
            <button type="button" class="close shadow hvr-buzz-out rounded-circle m-0" data-dismiss="modal" aria-label="Close">
              <i class="fas fa-times"></i>
            </button>
          </div>
          <div class="modal-body">
            <div class="form-group">
                <label class="fnt-hind">Title:*</label>
                <input type="text" v-model="title" class="form-control fnt-montserrat-alternates" placeholder="Task Name">
            </div>

            <div class="form-group">
                <label for="exampleInputPassword1">Deadline:</label>
                <input type="date" v-model="deadline" class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div>

            <div class="form-group">
                <label class="fnt-hind">Description:</label>
                <textarea v-model="description" class="form-control fnt-montserrat-alternates" placeholder="Task Description" rows="4"></textarea>
            </div>
          </div>
          <div class="modal-footer p-0 m-0">
            <button type="button" class="btn btn-primary btn-lg btn-block p-0 m-0 rounded-0 py-3" @click="saveTask">Save Task</button>
          </div>
        </div>
      </div>
    </div>
</template>

<style>
    #mdlNewTask .modal-header {
        background: #BF3056;
        position: relative;
    }

    #mdlNewTask .modal-body .form-group {
        display: flex;
        flex-direction: column;
    }

    #mdlNewTask .modal-body .form-group label {
        font-size: 1.6rem;
        text-transform: uppercase;
        color: #8C233F;
        text-align: left;
        letter-spacing: 1px;
    }

    #mdlNewTask .modal-body .form-group input,
    #mdlNewTask .modal-body .form-group textarea {
        font-size: 1.6rem;
    }

    #mdlNewTask .modal-body .form-group input:focus,
    #mdlNewTask .modal-body .form-group textarea:focus {
        border-color: #F23869;
        box-shadow: 0 0 0 0.2rem rgba(242, 56, 105,.25)
    }

    #mdlNewTask .modal-header .title {
        color: white;
        font-family: 'Bebas Neue', cursive;
        font-size: 2.5rem;
        letter-spacing: 1px;
        margin: 0px;
        padding: 0px;
    }

    #mdlNewTask .modal-header .title i {
        font-size: 1.7rem;
    }

    #mdlNewTask .modal-header small {
        color: #D9D9D9;
        font-family: 'Hind Siliguri', sans-serif;
        font-weight: 300;
        font-size: 1.4rem;
        text-align: left;
        display: block;
        margin-top: -9px;
    }

    #mdlNewTask .modal-header small strong{
        text-transform: uppercase;
    }

    #mdlNewTask .modal-header button {
        position: absolute;
        top: 10px;
        right: 14px;
        background: #8C233F !important;
        width: 45px;
        height: 45px;
        color: white;
        opacity: 1;
        font-size: 2rem;
    }

    #mdlNewTask .modal-content{
        border-bottom-right-radius: 20px !important;
        border: none !important;
        overflow: hidden;
    }

    #mdlNewTask .modal-footer button {
        background: #BF3056 !important;
        font-family: 'Montserrat Alternates', sans-serif;
        font-size: 2rem;
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 1px;
    }
</style>

<script>
import clientAxio from '@/tools/axios'

export default {
    name: 'ModalNewTask',
    props: {
      current: Object  
    },
    data() {
        return {
            title: '',
            description: '',
            deadline: null
        }
    },
    methods: {
        saveTask() {
            var me = this;

            let data = {
                title: me.title,
                description: me.description,
                deadline: me.deadline,
                group: me.current.id,
                tag: 'important'
            }

            clientAxio.post('tasks/', data).then(response => {
                console.log(response);
                $('#mdlNewTask').modal('hide');
                this.$emit("reloadGroup");
                me.title = "";
                me.description = "";
                me.deadline = null;
            });
        }
    },
    created() {
        $('#mdlNewTask').modal({});
    },
}
</script>
