from django.http import JsonResponse
from .models import Project, Deal
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create_deal(request):
    if request.method == 'POST':
        data = request.POST
        try:
            deal_name = data['deal_name']
            project_name = data['project_name']
            fmv = float(data['fmv'])
            tax_credit_transfer_rate = float(data['tax_credit_transfer_rate'])
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)
        except ValueError:
            return JsonResponse({"error": "Invalid field value"}, status=400)
        
        try:
            deal = Deal.objects.get(name=deal_name)
        except Deal.DoesNotExist:
            deal = Deal.objects.create(name=deal_name)
        
        project, created = Project.objects.get_or_create(name=project_name, defaults={'fmv': fmv, 'tax_credit_transfer_rate': tax_credit_transfer_rate})
        project.tax_credit_transfer_amount = fmv * 0.3 * tax_credit_transfer_rate
        project.save()
        
        deal.projects.add(project)
        update_deal_tax_credit_transfer_amount(deal)
        
        return JsonResponse({"id": deal.id, "name": deal.name}, status=201)


def update_deal_tax_credit_transfer_amount(deal):
    total_amount = sum(project.tax_credit_transfer_amount for project in deal.projects.all())
    deal.tax_credit_transfer_amount = total_amount
    deal.save()

def deal_tax_credit_transfer(request, deal_name):
    if request.method == 'GET':
        try:
            deal = Deal.objects.get(name=deal_name)
        except Deal.DoesNotExist:
            return JsonResponse({"error": "Deal not found"}, status=404)
        
        project_amounts = {project.name: project.tax_credit_transfer_amount for project in deal.projects.all()}
        return JsonResponse({"deal_name": deal.name, "tax_credit_transfer_amount": deal.tax_credit_transfer_amount, "project_tax_credit_transfer_amounts": project_amounts})
