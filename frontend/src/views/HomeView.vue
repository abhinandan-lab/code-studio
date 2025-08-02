<script setup>
import { onMounted } from 'vue'
import { useFileStore } from '../stores/fileStore'
import Codemirror from 'vue-codemirror'
import { javascript } from '@codemirror/lang-javascript'
import { python } from '@codemirror/lang-python'
import { oneDark } from '@codemirror/theme-one-dark'
// import EditorComponent from './components/EditorComponent.vue'

const store = useFileStore()

onMounted(() => store.fetchFiles())
</script>

<template>
  <div class="layout">
    <aside>
      <h3>Files</h3>
      <ul>
        <li v-for="f in store.files" :key="f" :class="{ active: f === store.activePath }" @click="store.loadFile(f)">
          {{ f }}
        </li>
      </ul>
    </aside>

    <section class="editor">
      <textarea v-model="store.code" rows="25"></textarea>

      <!-- HomeView.vue – replace the self-closed tag -->
      <!-- <codemirror v-model="code" placeholder="Code goes here..." :style="{ height: '400px' }" :autofocus="true"
        :indent-with-tab="true" :tab-size="2" :extensions="extensions" @ready="handleReady"
        @change="log('change', $event)" @focus="log('focus', $event)" @blur="log('blur', $event)" /> -->


      <!-- <EditorComponent /> -->



      <div class="buttons">
        <button @click="store.saveCode">Save Code</button>
        <button @click="store.deploy">Update Live</button>
      </div>

      <iframe src="http://localhost:5200" title="Live Preview"></iframe>
    </section>
  </div>
</template>

<style scoped lang="scss">
.layout {
  display: flex;
  gap: 1rem;
}

aside {
  width: 200px;
  border-right: 1px solid #ccc;
  overflow: auto;

  ul {
    list-style: none;
    padding: 0;
    margin: 0;
    height: 90dvh;

    li {
      padding: 4px 6px;
      cursor: pointer;

      &.active {
        background: #eef;
        font-weight: bold;
      }
    }
  }
}

.editor {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;

  textarea {
    flex: 1;
    font-family: monospace;
  }

  .buttons {
    display: flex;
    gap: 0.5rem;
  }

  iframe {
    flex: 1;
    border: 1px solid #ccc;
  }
}
</style>
