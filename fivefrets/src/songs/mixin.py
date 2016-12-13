class GetSongContextMixin(object):
    slug_field = 'youtube'

    def get_context_data(self, **kwargs):
        context = super(GetSongContextMixin, self).get_context_data(**kwargs)
        context['song_meta'] = self.get_object().get_song_meta()
        context['songchord_list'] = self.get_object().get_songchord_list()
        context['chords'] = self.get_object().get_song_chords()
        return context
