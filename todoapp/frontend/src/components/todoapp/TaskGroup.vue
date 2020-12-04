<template>
  <li class="my-2 taskgroup hvr-icon-pop" :class="{ 'isOpen': group.show }" @click="taskGroupClick">
      <span class="icon mr-3"> 
          <i class="fas fa-folder hvr-icon" v-if="!group.show"></i>
          <i class="fas fa-folder-open hvr-icon" v-else></i>
      </span>
      {{ group.title }}
  </li>
</template>

<style>
  li.taskgroup {
    color: #D9D9D9;
    font-family: 'Hind Siliguri', sans-serif;
    text-align: left;
    font-size: 2rem;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 1px;
    cursor: pointer;

    display: list-item !important;
  }

  li.taskgroup.isOpen {
    padding-left: 10px;
  }
</style>

<script>
export default {
  name: 'TaskGroup',
  props: {
    group: Object,
  },
  data() {
    return {
      isSelect: false
    }
  },
  methods: {
    taskGroupClick(e) {
      this.$emit("onClicked", this.group);
    }
  },
}
</script>
