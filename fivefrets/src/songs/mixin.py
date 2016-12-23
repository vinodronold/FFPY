class GetSongContextMixin(object):
    slug_field = 'youtube'

    def get_context_data(self, **kwargs):
        context = super(GetSongContextMixin, self).get_context_data(**kwargs)
        context['song_meta'] = self.get_object().get_song_meta()
        context['songchord_list'] = self.get_object().get_songchord_list()
        context['chords'] = self.get_object().get_song_chords()
        return context


class SongPaginationMixin(object):
    paginate_by = 12

    def paginate_queryset(self, queryset, page_size):
        """
        Paginate the queryset, if needed.
        """
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(
            page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
            if page_number > paginator.num_pages:
                page_number = paginator.num_pages
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                page_number = 1
        page = paginator.page(page_number)
        return (paginator, page, page.object_list, page.has_other_pages())
