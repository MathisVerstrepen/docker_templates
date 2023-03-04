<template>
    <div>
        <!-- I18n language selection example -->
        <select v-model="locale">
            <option value="en">en</option>
            <option value="fr">fr</option>
        </select>
        <p>{{ $t('welcome') }}</p>

        <h1>My Nuxt 3 App</h1>

        <p>{{useCounterStore.doubleCount}}</p>
    </div>
</template>

<script setup lang="ts">
const { locale } = useI18n()
</script>