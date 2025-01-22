TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                # ... existing processors ...
                'blog.context_processors.categories_processor',
            ],
        },
    },
] 