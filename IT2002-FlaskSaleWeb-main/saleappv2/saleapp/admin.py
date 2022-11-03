from saleapp.models import Category, Product
from saleapp import db,app,login
from flask_admin import Admin,BaseView,expose
from flask_admin.contrib.sqla import ModelView


class ProductModel(ModelView):
    column_searchable_list = ['name','description']
    column_filters = ['id','name']
    column_export_list = ['id','name','price']
    column_exclude_list = ['image']
    column_labels = {
        'name': 'Tên sản phẩm',
        'description': 'Chi tiết sản phẩm',
        'price': 'Giá',
        'active': 'Tình trạng',
        'category': 'Loại sản phẩm'
    }
    can_export = True
    can_view_details = True

class StasModel(BaseView):
    @expose('/')
    def __index__(self):
        return self.render('admin/stas.html')
admin = Admin(app= app, name='Quản trị bán hàng', template_mode='bootstrap4')
admin.add_view(ModelView(Category, db.session,name='Mặt hàng'))
admin.add_view(ProductModel(Product, db.session, name='Sản phẩm'))
admin.add_view(StasModel(name='Thống kê báo cáo'))