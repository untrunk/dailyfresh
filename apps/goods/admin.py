from django.contrib import admin
from django.core.cache import cache
from apps.goods.models import GoodsType,IndexPromotionBanner,IndexGoodsBanner,IndexTypeGoodsBanner,Goods,GoodsSKU
from celery_tasks.tasks import generate_static_index_html


# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''新增或更表中到数据时调用'''
        super().save_model(request,obj,form,change)

        # 发出任务，让celery worker 重新生成首页静态页

        generate_static_index_html.delay()

        #清楚首页的缓存
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        '''删除表中到数据时调用'''
        super().delete_model(request,obj)
        generate_static_index_html.delay()

        # 清楚首页的缓存
        cache.delete('index_page_data')

class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass

class GoodsTypeAdmin(BaseModelAdmin):
    pass

class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass

class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass

admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(IndexPromotionBanner,IndexPromotionBannerAdmin)
admin.site.register(IndexGoodsBanner,IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner,IndexTypeGoodsBannerAdmin)
admin.site.register(Goods)
admin.site.register(GoodsSKU)