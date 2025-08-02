<template>
  <div>
    <codemirror
      v-model="code"
      placeholder="Write some JS code..."
      :style="{ height: '300px', border: '1px solid #333' }"
      :autofocus="true"
      :tab-size="2"
      :extensions="extensions"
      @ready="handleReady"
    />

    <h3>Live Preview</h3>
    <pre>{{ code }}</pre>
  </div>
</template>

<script setup>
import { ref, shallowRef } from 'vue'
import { Codemirror } from 'vue-codemirror'
import { javascript } from '@codemirror/lang-javascript'
import { oneDark } from '@codemirror/theme-one-dark'

const code = ref(`console.log('Hello from CodeMirror!')`)
const extensions = [javascript(), oneDark]

const view = shallowRef(null)
const handleReady = ({ view: editorView }) => {
  view.value = editorView
}
</script>
