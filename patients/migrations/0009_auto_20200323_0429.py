# Generated by Django 3.0.4 on 2020-03-22 22:59

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_auto_20200322_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='detected_district',
            field=models.CharField(blank=True, choices=[('Narayanpet', 'Narayanpet'), ('Jayashankar', 'Jayashankar'), ('Bhadradri Kothagudem', 'Bhadradri Kothagudem'), ('Yadadri Bhuvanagiri', 'Yadadri Bhuvanagiri'), ('Warangal Urban', 'Warangal Urban'), ('Warangal Rural', 'Warangal Rural'), ('Wanaparthy', 'Wanaparthy'), ('Vikarabad', 'Vikarabad'), ('Suryapet', 'Suryapet'), ('Siddipet', 'Siddipet'), ('Sangareddy', 'Sangareddy'), ('Ranga Reddy', 'Ranga Reddy'), ('Rajanna Sircilla', 'Rajanna Sircilla'), ('Peddapalli', 'Peddapalli'), ('Nizamabad', 'Nizamabad'), ('Nirmal', 'Nirmal'), ('Nalgonda', 'Nalgonda'), ('Nagarkurnool', 'Nagarkurnool'), ('Medchal Malkajgiri', 'Medchal Malkajgiri'), ('Medak', 'Medak'), ('Mancherial', 'Mancherial'), ('Mahabubnagar', 'Mahabubnagar'), ('Mahabubabad', 'Mahabubabad'), ('Kumuram Bheem Asifabad', 'Kumuram Bheem Asifabad'), ('Khammam', 'Khammam'), ('Karimnagar', 'Karimnagar'), ('Kamareddy', 'Kamareddy'), ('Jogulamba Gadwal', 'Jogulamba Gadwal'), ('Mulugu', 'Mulugu'), ('Jangoan', 'Jangoan'), ('Jagitial', 'Jagitial'), ('Hyderabad', 'Hyderabad'), ('Adilabad', 'Adilabad'), ('Yanam', 'Yanam'), ('Mahe', 'Mahe'), ('Karaikal', 'Karaikal'), ('Puducherry', 'Puducherry'), ('Vijayapura', 'Vijayapura'), ('Mysuru', 'Mysuru'), ('Mandya', 'Mandya'), ('Ramanagara', 'Ramanagara'), ('Tumakuru', 'Tumakuru'), ('Chamarajanagara', 'Chamarajanagara'), ('Kodagu', 'Kodagu'), ('Bengaluru', 'Bengaluru'), ('Dakshina Kannada', 'Dakshina Kannada'), ('Bengaluru Rural', 'Bengaluru Rural'), ('Kolar', 'Kolar'), ('Hassan', 'Hassan'), ('Chikkaballapura', 'Chikkaballapura'), ('Chikkamagaluru', 'Chikkamagaluru'), ('Udupi', 'Udupi'), ('Shivamogga', 'Shivamogga'), ('Davanagere', 'Davanagere'), ('Chitradurga', 'Chitradurga'), ('Haveri', 'Haveri'), ('Uttara Kannada', 'Uttara Kannada'), ('Dharwad', 'Dharwad'), ('Ballari', 'Ballari'), ('Gadag', 'Gadag'), ('Koppal', 'Koppal'), ('Raichur', 'Raichur'), ('Bagalkote', 'Bagalkote'), ('Yadgir', 'Yadgir'), ('Belagavi', 'Belagavi'), ('Kalaburagi', 'Kalaburagi'), ('Bidar', 'Bidar'), ('Chandigarh', 'Chandigarh'), ('Bilaspur', 'Bilaspur'), ('Hamirpur', 'Hamirpur'), ('Sirmaur', 'Sirmaur'), ('Solan', 'Solan'), ('Shimla', 'Shimla'), ('Una', 'Una'), ('Kinnaur', 'Kinnaur'), ('Mandi', 'Mandi'), ('Kullu', 'Kullu'), ('Kangra', 'Kangra'), ('Chamba', 'Chamba'), ('Lahul & Spiti', 'Lahul & Spiti'), ('Pratapgarh', 'Pratapgarh'), ('Bikaner', 'Bikaner'), ('Hanumangarh', 'Hanumangarh'), ('Ganganagar', 'Ganganagar'), ('Chittaurgarh', 'Chittaurgarh'), ('Rajsamand', 'Rajsamand'), ('Ajmer', 'Ajmer'), ('Banswara', 'Banswara'), ('Dungarpur', 'Dungarpur'), ('Jhalawar', 'Jhalawar'), ('Udaipur', 'Udaipur'), ('Baran', 'Baran'), ('Sirohi', 'Sirohi'), ('Kota', 'Kota'), ('Bundi', 'Bundi'), ('Jalor', 'Jalor'), ('Bhilwara', 'Bhilwara'), ('Pali', 'Pali'), ('Tonk', 'Tonk'), ('Sawai Madhopur', 'Sawai Madhopur'), ('Barmer', 'Barmer'), ('Dhaulpur', 'Dhaulpur'), ('Karauli', 'Karauli'), ('Dausa', 'Dausa'), ('Nagaur', 'Nagaur'), ('Bharatpur', 'Bharatpur'), ('Jodhpur', 'Jodhpur'), ('Jaipur', 'Jaipur'), ('Alwar', 'Alwar'), ('Sikar', 'Sikar'), ('Jaisalmer', 'Jaisalmer'), ('Jhunjhunu', 'Jhunjhunu'), ('Churu', 'Churu'), ('Lawngtlai', 'Lawngtlai'), ('Saiha', 'Saiha'), ('Lunglei', 'Lunglei'), ('Serchhip', 'Serchhip'), ('Champhai', 'Champhai'), ('Mamit', 'Mamit'), ('Aizawl', 'Aizawl'), ('Kolasib', 'Kolasib'), ('Balrampur', 'Balrampur'), ('Surguja', 'Surguja'), ('Surajpur', 'Surajpur'), ('Korba', 'Korba'), ('Jashpur', 'Jashpur'), ('Koriya', 'Koriya'), ('Sukma', 'Sukma'), ('Bilaspur', 'Bilaspur'), ('Raigarh', 'Raigarh'), ('Bijapur', 'Bijapur'), ('Mungeli', 'Mungeli'), ('Baloda Bazar', 'Baloda Bazar'), ('Rajnandgaon', 'Rajnandgaon'), ('Bametara', 'Bametara'), ('Janjgir - Champa', 'Janjgir - Champa'), ('Kabeerdham', 'Kabeerdham'), ('Balod', 'Balod'), ('Dhamtari', 'Dhamtari'), ('Durg', 'Durg'), ('Raipur', 'Raipur'), ('Gariaband', 'Gariaband'), ('Kondagaon', 'Kondagaon'), ('Bastar', 'Bastar'), ('Dakshin Bastar Dantewada', 'Dakshin Bastar Dantewada'), ('Narayanpur', 'Narayanpur'), ('Uttar Bastar Kanker', 'Uttar Bastar Kanker'), ('Mahasamund', 'Mahasamund'), ('Sambalpur', 'Sambalpur'), ('Debagarh', 'Debagarh'), ('Bargarh', 'Bargarh'), ('Jharsuguda', 'Jharsuguda'), ('Baleshwar', 'Baleshwar'), ('Kendujhar', 'Kendujhar'), ('Sundargarh', 'Sundargarh'), ('Mayurbhanj', 'Mayurbhanj'), ('Gajapati', 'Gajapati'), ('Ganjam', 'Ganjam'), ('Kendrapara', 'Kendrapara'), ('Anugul', 'Anugul'), ('Malkangiri', 'Malkangiri'), ('Koraput', 'Koraput'), ('Rayagada', 'Rayagada'), ('Nabarangapur', 'Nabarangapur'), ('Puri', 'Puri'), ('Jagatsinghapur', 'Jagatsinghapur'), ('Kalahandi', 'Kalahandi'), ('Khordha', 'Khordha'), ('Nayagarh', 'Nayagarh'), ('Kandhamal', 'Kandhamal'), ('Cuttack', 'Cuttack'), ('Baudh', 'Baudh'), ('Balangir', 'Balangir'), ('Nuapada', 'Nuapada'), ('Subarnapur', 'Subarnapur'), ('Jajapur', 'Jajapur'), ('Dhenkanal', 'Dhenkanal'), ('Bhadrak', 'Bhadrak'), ('Kannur', 'Kannur'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Ernakulam', 'Ernakulam'), ('Idukki', 'Idukki'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'), ('Kasaragod', 'Kasaragod'), ('Kargil', 'Kargil'), ('Leh', 'Leh'), ('Ramanathapuram', 'Ramanathapuram'), ('Sivaganga', 'Sivaganga'), ('Pudukkottai', 'Pudukkottai'), ('Nagapattinam', 'Nagapattinam'), ('Cuddalore', 'Cuddalore'), ('Viluppuram', 'Viluppuram'), ('Kanniyakumari', 'Kanniyakumari'), ('Thoothukkudi', 'Thoothukkudi'), ('Tirunelveli', 'Tirunelveli'), ('Virudhunagar', 'Virudhunagar'), ('Theni', 'Theni'), ('Madurai', 'Madurai'), ('Dindigul', 'Dindigul'), ('Thiruvarur', 'Thiruvarur'), ('Karur', 'Karur'), ('Thanjavur', 'Thanjavur'), ('Tiruppur', 'Tiruppur'), ('Ariyalur', 'Ariyalur'), ('Tiruchirappalli', 'Tiruchirappalli'), ('Coimbatore', 'Coimbatore'), ('Perambalur', 'Perambalur'), ('Namakkal', 'Namakkal'), ('The Nilgiris', 'The Nilgiris'), ('Erode', 'Erode'), ('Salem', 'Salem'), ('Dharmapuri', 'Dharmapuri'), ('Tiruvannamalai', 'Tiruvannamalai'), ('Krishnagiri', 'Krishnagiri'), ('Kancheepuram', 'Kancheepuram'), ('Chennai', 'Chennai'), ('Vellore', 'Vellore'), ('Thiruvallur', 'Thiruvallur'), ('Dimapur', 'Dimapur'), ('Kohima', 'Kohima'), ('Phek', 'Phek'), ('Zunheboto', 'Zunheboto'), ('Wokha', 'Wokha'), ('Peren', 'Peren'), ('Kiphire', 'Kiphire'), ('Tuensang', 'Tuensang'), ('Mokokchung', 'Mokokchung'), ('Longleng', 'Longleng'), ('Mon', 'Mon'), ('Niwari', 'Niwari'), ('Panna', 'Panna'), ('Chhatarpur', 'Chhatarpur'), ('Datia', 'Datia'), ('Agar Malwa', 'Agar Malwa'), ('Hoshangabad', 'Hoshangabad'), ('Mandla', 'Mandla'), ('Indore', 'Indore'), ('Dhar', 'Dhar'), ('Narsimhapur', 'Narsimhapur'), ('Dindori', 'Dindori'), ('Jhabua', 'Jhabua'), ('Anuppur', 'Anuppur'), ('Dewas', 'Dewas'), ('Jabalpur', 'Jabalpur'), ('Sehore', 'Sehore'), ('Raisen', 'Raisen'), ('Ujjain', 'Ujjain'), ('Bhopal', 'Bhopal'), ('Ratlam', 'Ratlam'), ('Umaria', 'Umaria'), ('Katni', 'Katni'), ('Shahdol', 'Shahdol'), ('Rajgarh', 'Rajgarh'), ('Vidisha', 'Vidisha'), ('Shajapur', 'Shajapur'), ('Damoh', 'Damoh'), ('Sagar', 'Sagar'), ('Sidhi', 'Sidhi'), ('Singrauli', 'Singrauli'), ('Mandsaur', 'Mandsaur'), ('Ashoknagar', 'Ashoknagar'), ('Guna', 'Guna'), ('Satna', 'Satna'), ('Rewa', 'Rewa'), ('Neemuch', 'Neemuch'), ('Tikamgarh', 'Tikamgarh'), ('Shivpuri', 'Shivpuri'), ('Sheopur', 'Sheopur'), ('Gwalior', 'Gwalior'), ('Bhind', 'Bhind'), ('Morena', 'Morena'), ('Betul', 'Betul'), ('Barwani', 'Barwani'), ('Balaghat', 'Balaghat'), ('East Nimar', 'East Nimar'), ('West Nimar', 'West Nimar'), ('Harda', 'Harda'), ('Chhindwara', 'Chhindwara'), ('Alirajpur', 'Alirajpur'), ('Seoni', 'Seoni'), ('Burhanpur', 'Burhanpur'), ('South Goa', 'South Goa'), ('North Goa', 'North Goa'), ('East District', 'East District'), ('South District', 'South District'), ('West District', 'West District'), ('North District', 'North District'), ('Aurangabad', 'Aurangabad'), ('Kishanganj', 'Kishanganj'), ('Purnia', 'Purnia'), ('Madhubani', 'Madhubani'), ('Supaul', 'Supaul'), ('Araria', 'Araria'), ('Madhepura', 'Madhepura'), ('Muzaffarpur', 'Muzaffarpur'), ('Siwan', 'Siwan'), ('Saran', 'Saran'), ('Patna', 'Patna'), ('Nalanda', 'Nalanda'), ('Jehanabad', 'Jehanabad'), ('Arwal', 'Arwal'), ('Sheikhpura', 'Sheikhpura'), ('Lakhisarai', 'Lakhisarai'), ('Bhagalpur', 'Bhagalpur'), ('Begusarai', 'Begusarai'), ('Vaishali', 'Vaishali'), ('Munger', 'Munger'), ('Gaya', 'Gaya'), ('Nawada', 'Nawada'), ('Banka', 'Banka'), ('Jamui', 'Jamui'), ('Rohtas', 'Rohtas'), ('Kaimur (bhabua)', 'Kaimur (bhabua)'), ('Saharsa', 'Saharsa'), ('Darbhanga', 'Darbhanga'), ('Buxar', 'Buxar'), ('Bhojpur', 'Bhojpur'), ('Khagaria', 'Khagaria'), ('Katihar', 'Katihar'), ('Samastipur', 'Samastipur'), ('Gopalganj', 'Gopalganj'), ('Sheohar', 'Sheohar'), ('Sitamarhi', 'Sitamarhi'), ('Purba Champaran', 'Purba Champaran'), ('Pashchim Champaran', 'Pashchim Champaran'), ('Chittoor', 'Chittoor'), ('Y.S.R.', 'Y.S.R.'), ('West Godavari', 'West Godavari'), ('S.P.S. Nellore', 'S.P.S. Nellore'), ('Anantapur', 'Anantapur'), ('Kurnool', 'Kurnool'), ('Prakasam', 'Prakasam'), ('East Godavari', 'East Godavari'), ('Guntur', 'Guntur'), ('Krishna', 'Krishna'), ('Visakhapatnam', 'Visakhapatnam'), ('Vizianagaram', 'Vizianagaram'), ('Srikakulam', 'Srikakulam'), ('Hazaribagh', 'Hazaribagh'), ('Kodarma', 'Kodarma'), ('Simdega', 'Simdega'), ('Pashchimi Singhbhum', 'Pashchimi Singhbhum'), ('Purbi Singhbhum', 'Purbi Singhbhum'), ('Saraikela-kharsawan', 'Saraikela-kharsawan'), ('Khunti', 'Khunti'), ('Gumla', 'Gumla'), ('Lohardaga', 'Lohardaga'), ('Ranchi', 'Ranchi'), ('Ramgarh', 'Ramgarh'), ('Bokaro', 'Bokaro'), ('Latehar', 'Latehar'), ('Dhanbad', 'Dhanbad'), ('Jamtara', 'Jamtara'), ('Garhwa', 'Garhwa'), ('Chatra', 'Chatra'), ('Palamu', 'Palamu'), ('Deoghar', 'Deoghar'), ('Dumka', 'Dumka'), ('Giridih', 'Giridih'), ('Pakur', 'Pakur'), ('Godda', 'Godda'), ('Sahibganj', 'Sahibganj'), ('South West Garo Hills', 'South West Garo Hills'), ('North Garo Hills', 'North Garo Hills'), ('South West Khasi Hills', 'South West Khasi Hills'), ('West Jaintia Hills', 'West Jaintia Hills'), ('East Garo Hills', 'East Garo Hills'), ('West Garo Hills', 'West Garo Hills'), ('South Garo Hills', 'South Garo Hills'), ('East Khasi Hills', 'East Khasi Hills'), ('East Jaintia Hills', 'East Jaintia Hills'), ('West Khasi Hills', 'West Khasi Hills'), ('Ribhoi', 'Ribhoi'), ('North West Delhi', 'North West Delhi'), ('South East Delhi', 'South East Delhi'), ('Shahdara', 'Shahdara'), ('South Delhi', 'South Delhi'), ('New Delhi', 'New Delhi'), ('Central Delhi', 'Central Delhi'), ('South West Delhi', 'South West Delhi'), ('East Delhi', 'East Delhi'), ('West Delhi', 'West Delhi'), ('North East Delhi', 'North East Delhi'), ('North Delhi', 'North Delhi'), ('Uttar Dinajpur', 'Uttar Dinajpur'), ('Cooch Behar', 'Cooch Behar'), ('Kalimpong', 'Kalimpong'), ('Paschim Bardhaman', 'Paschim Bardhaman'), ('Alipurduar', 'Alipurduar'), ('Kolkata', 'Kolkata'), ('Howrah', 'Howrah'), ('Hooghly', 'Hooghly'), ('North 24 Parganas', 'North 24 Parganas'), ('Bankura', 'Bankura'), ('Puruliya', 'Puruliya'), ('Purba Bardhaman', 'Purba Bardhaman'), ('Nadia', 'Nadia'), ('Birbhum', 'Birbhum'), ('Murshidabad', 'Murshidabad'), ('Maldah', 'Maldah'), ('Dakshin Dinajpur', 'Dakshin Dinajpur'), ('Jalpaiguri', 'Jalpaiguri'), ('Darjeeling', 'Darjeeling'), ('Jhargram', 'Jhargram'), ('Purba Medinipur', 'Purba Medinipur'), ('Medinipur West', 'Medinipur West'), ('South 24 Parganas', 'South 24 Parganas'), ('West Karbi Anglong', 'West Karbi Anglong'), ('Karbi Anglong', 'Karbi Anglong'), ('South Salmara Mancachar', 'South Salmara Mancachar'), ('Hojai', 'Hojai'), ('Biswanath', 'Biswanath'), ('Majuli', 'Majuli'), ('Charaideo', 'Charaideo'), ('Hailakandi', 'Hailakandi'), ('Karimganj', 'Karimganj'), ('Cachar', 'Cachar'), ('Dima Hasao', 'Dima Hasao'), ('Goalpara', 'Goalpara'), ('Kamrup Metropolitan', 'Kamrup Metropolitan'), ('Dhubri', 'Dhubri'), ('Bongaigaon', 'Bongaigaon'), ('Kamrup', 'Kamrup'), ('Morigaon', 'Morigaon'), ('Nalbari', 'Nalbari'), ('Barpeta', 'Barpeta'), ('Darrang', 'Darrang'), ('Kokrajhar', 'Kokrajhar'), ('Nagaon', 'Nagaon'), ('Baksa', 'Baksa'), ('Chirang', 'Chirang'), ('Udalguri', 'Udalguri'), ('Golaghat', 'Golaghat'), ('Sonitpur', 'Sonitpur'), ('Jorhat', 'Jorhat'), ('Sivasagar', 'Sivasagar'), ('Lakhimpur', 'Lakhimpur'), ('Dibrugarh', 'Dibrugarh'), ('Dhemaji', 'Dhemaji'), ('Tinsukia', 'Tinsukia'), ('Lakshadweep', 'Lakshadweep'), ('Nicobars', 'Nicobars'), ('South Andaman', 'South Andaman'), ('North & Middle Andaman', 'North & Middle Andaman'), ('Kamle', 'Kamle'), ('Lepa Rada', 'Lepa Rada'), ('West Siang', 'West Siang'), ('Pakke Kessang', 'Pakke Kessang'), ('Shi Yomi', 'Shi Yomi'), ('Siang', 'Siang'), ('Lower Dibang Valley', 'Lower Dibang Valley'), ('Upper Dibang Valley', 'Upper Dibang Valley'), ('Lower Siang', 'Lower Siang'), ('Upper Siang', 'Upper Siang'), ('Longding', 'Longding'), ('Namsai', 'Namsai'), ('Kra Daadi', 'Kra Daadi'), ('West Kamenghttps://github.com/covid19india/CovidCrowd/issues/6', 'West Kamenghttps://github.com/covid19india/CovidCrowd/issues/6'), ('East Kameng', 'East Kameng'), ('Lower Subansiri', 'Lower Subansiri'), ('Kurung Kumey', 'Kurung Kumey'), ('Lohit', 'Lohit'), ('East Siang', 'East Siang'), ('Tirap', 'Tirap'), ('Papum Pare', 'Papum Pare'), ('Tawang', 'Tawang'), ('Changlang', 'Changlang'), ('Anjaw', 'Anjaw'), ('Upper Subansiri', 'Upper Subansiri'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Mirpur', 'Mirpur'), ('Muzaffarabad', 'Muzaffarabad'), ('Samba', 'Samba'), ('Udhampur', 'Udhampur'), ('Kathua', 'Kathua'), ('Jammu', 'Jammu'), ('Doda', 'Doda'), ('Reasi', 'Reasi'), ('Ramban', 'Ramban'), ('Rajouri', 'Rajouri'), ('Kulgam', 'Kulgam'), ('Shupiyan', 'Shupiyan'), ('Punch', 'Punch'), ('Pulwama', 'Pulwama'), ('Badgam', 'Badgam'), ('Srinagar', 'Srinagar'), ('Kishtwar', 'Kishtwar'), ('Anantnag', 'Anantnag'), ('Ganderbal', 'Ganderbal'), ('Baramula', 'Baramula'), ('Bandipore', 'Bandipore'), ('Kupwara', 'Kupwara'), ('Ambala', 'Ambala'), ('Panchkula', 'Panchkula'), ('Rohtak', 'Rohtak'), ('Bhiwani', 'Bhiwani'), ('Sonipat', 'Sonipat'), ('Panipat', 'Panipat'), ('Hisar', 'Hisar'), ('Fatehabad', 'Fatehabad'), ('Jind', 'Jind'), ('Karnal', 'Karnal'), ('Sirsa', 'Sirsa'), ('Kaithal', 'Kaithal'), ('Kurukshetra', 'Kurukshetra'), ('Yamunanagar', 'Yamunanagar'), ('Charki Dadri', 'Charki Dadri'), ('Palwal', 'Palwal'), ('Nuh', 'Nuh'), ('Rewari', 'Rewari'), ('Mahendragarh', 'Mahendragarh'), ('Faridabad', 'Faridabad'), ('Gurugram', 'Gurugram'), ('Jhajjar', 'Jhajjar'), ('Diu', 'Diu'), ('Daman', 'Daman'), ('Udham Singh Nagar', 'Udham Singh Nagar'), ('Champawat', 'Champawat'), ('Nainital', 'Nainital'), ('Almora', 'Almora'), ('Pauri Garhwal', 'Pauri Garhwal'), ('Hardwar', 'Hardwar'), ('Bageshwar', 'Bageshwar'), ('Pithoragarh', 'Pithoragarh'), ('Rudraprayag', 'Rudraprayag'), ('Tehri Garhwal', 'Tehri Garhwal'), ('Dehradun', 'Dehradun'), ('Chamoli', 'Chamoli'), ('Uttarkashi', 'Uttarkashi'), ('Kapurthala', 'Kapurthala'), ('Pathankot', 'Pathankot'), ('Firozpur', 'Firozpur'), ('Mansa', 'Mansa'), ('Patiala', 'Patiala'), ('Bathinda', 'Bathinda'), ('Barnala', 'Barnala'), ('Sangrur', 'Sangrur'), ('Sri Muktsar Sahib', 'Sri Muktsar Sahib'), ('Fatehgarh Sahib', 'Fatehgarh Sahib'), ('Faridkot', 'Faridkot'), ('S.A.S. Nagar', 'S.A.S. Nagar'), ('Ludhiana', 'Ludhiana'), ('Moga', 'Moga'), ('Fazilka', 'Fazilka'), ('Shahid Bhagat Singh Nagar', 'Shahid Bhagat Singh Nagar'), ('Rupnagar', 'Rupnagar'), ('Tarn Taran', 'Tarn Taran'), ('Jalandhar', 'Jalandhar'), ('Amritsar', 'Amritsar'), ('Hoshiarpur', 'Hoshiarpur'), ('Gurdaspur', 'Gurdaspur'), ('Pratapgarh', 'Pratapgarh'), ('Hamirpur', 'Hamirpur'), ('Balrampur', 'Balrampur'), ('Shamli', 'Shamli'), ('Rampur', 'Rampur'), ('Moradabad', 'Moradabad'), ('Meerut', 'Meerut'), ('Baghpat', 'Baghpat'), ('Muzaffarnagar', 'Muzaffarnagar'), ('Bijnor', 'Bijnor'), ('Saharanpur', 'Saharanpur'), ('Mahoba', 'Mahoba'), ('Sambhal', 'Sambhal'), ('Ghaziabad', 'Ghaziabad'), ('Amethi', 'Amethi'), ('Sonbhadra', 'Sonbhadra'), ('Lalitpur', 'Lalitpur'), ('Mirzapur', 'Mirzapur'), ('Bhadohi', 'Bhadohi'), ('Chandauli', 'Chandauli'), ('Chitrakoot', 'Chitrakoot'), ('Varanasi', 'Varanasi'), ('Prayagraj', 'Prayagraj'), ('Kaushambi', 'Kaushambi'), ('Ghazipur', 'Ghazipur'), ('Banda', 'Banda'), ('Jhansi', 'Jhansi'), ('Jaunpur', 'Jaunpur'), ('Ballia', 'Ballia'), ('Fatehpur', 'Fatehpur'), ('Mau', 'Mau'), ('Azamgarh', 'Azamgarh'), ('Jalaun', 'Jalaun'), ('Rae Bareli', 'Rae Bareli'), ('Ambedkar Nagar', 'Ambedkar Nagar'), ('Sultanpur', 'Sultanpur'), ('Deoria', 'Deoria'), ('Kanpur Dehat', 'Kanpur Dehat'), ('Faizabad', 'Faizabad'), ('Auraiya', 'Auraiya'), ('Kanpur Nagar', 'Kanpur Nagar'), ('Etawah', 'Etawah'), ('Unnao', 'Unnao'), ('Sant Kabir Nagar', 'Sant Kabir Nagar'), ('Gorakhpur', 'Gorakhpur'), ('Basti', 'Basti'), ('Lucknow', 'Lucknow'), ('Kannauj', 'Kannauj'), ('Kushinagar', 'Kushinagar'), ('Bara Banki', 'Bara Banki'), ('Gonda', 'Gonda'), ('Agra', 'Agra'), ('Mahrajganj', 'Mahrajganj'), ('Mainpuri', 'Mainpuri'), ('Siddharthnagar', 'Siddharthnagar'), ('Firozabad', 'Firozabad'), ('Farrukhabad', 'Farrukhabad'), ('Hardoi', 'Hardoi'), ('Etah', 'Etah'), ('Hathras', 'Hathras'), ('Sitapur', 'Sitapur'), ('Shrawasti', 'Shrawasti'), ('Mathura', 'Mathura'), ('Kasganj', 'Kasganj'), ('Aligarh', 'Aligarh'), ('Shahjahanpur', 'Shahjahanpur'), ('Bahraich', 'Bahraich'), ('Budaun', 'Budaun'), ('Kheri', 'Kheri'), ('Gautam Buddha Nagar', 'Gautam Buddha Nagar'), ('Bulandshahr', 'Bulandshahr'), ('Pilibhit', 'Pilibhit'), ('Bareilly', 'Bareilly'), ('Hapur', 'Hapur'), ('Amroha', 'Amroha'), ('Morbi', 'Morbi'), ('Anand', 'Anand'), ('Kheda', 'Kheda'), ('Surendranagar', 'Surendranagar'), ('Kachchh', 'Kachchh'), ('Sabar Kantha', 'Sabar Kantha'), ('Mahisagar', 'Mahisagar'), ('Aravalli', 'Aravalli'), ('Dohad', 'Dohad'), ('Panch Mahals', 'Panch Mahals'), ('Ahmadabad', 'Ahmadabad'), ('Gandhinagar', 'Gandhinagar'), ('Mahesana', 'Mahesana'), ('Patan', 'Patan'), ('Banas Kantha', 'Banas Kantha'), ('Navsari', 'Navsari'), ('Devbhumi Dwarka', 'Devbhumi Dwarka'), ('Jamnagar', 'Jamnagar'), ('Junagadh', 'Junagadh'), ('Bhavnagar', 'Bhavnagar'), ('Rajkot', 'Rajkot'), ('Gir Somnath', 'Gir Somnath'), ('Chota Udaipur', 'Chota Udaipur'), ('Botad', 'Botad'), ('Tapi', 'Tapi'), ('Surat', 'Surat'), ('Narmada', 'Narmada'), ('Porbandar', 'Porbandar'), ('Bharuch', 'Bharuch'), ('Vadodara', 'Vadodara'), ('The Dangs', 'The Dangs'), ('Amreli', 'Amreli'), ('Valsad', 'Valsad'), ('Mumbai Suburban', 'Mumbai Suburban'), ('Raigarh', 'Raigarh'), ('Aurangabad', 'Aurangabad'), ('Nagpur', 'Nagpur'), ('Dhule', 'Dhule'), ('Amravati', 'Amravati'), ('Nandurbar', 'Nandurbar'), ('Palghar', 'Palghar'), ('Thane', 'Thane'), ('Sindhudurg', 'Sindhudurg'), ('Kolhapur', 'Kolhapur'), ('Sangli', 'Sangli'), ('Ratnagiri', 'Ratnagiri'), ('Satara', 'Satara'), ('Solapur', 'Solapur'), ('Osmanabad', 'Osmanabad'), ('Latur', 'Latur'), ('Mumbai', 'Mumbai'), ('Bid', 'Bid'), ('Pune', 'Pune'), ('Parbhani', 'Parbhani'), ('Nanded', 'Nanded'), ('Hingoli', 'Hingoli'), ('Ahmadnagar', 'Ahmadnagar'), ('Jalna', 'Jalna'), ('Yavatmal', 'Yavatmal'), ('Chandrapur', 'Chandrapur'), ('Washim', 'Washim'), ('Gadchiroli', 'Gadchiroli'), ('Nashik', 'Nashik'), ('Akola', 'Akola'), ('Buldana', 'Buldana'), ('Wardha', 'Wardha'), ('Jalgaon', 'Jalgaon'), ('Bhandara', 'Bhandara'), ('Gondiya', 'Gondiya'), ('Unokoti', 'Unokoti'), ('South Tripura', 'South Tripura'), ('West Tripura', 'West Tripura'), ('Khowai', 'Khowai'), ('Gomati', 'Gomati'), ('Sipahijala', 'Sipahijala'), ('Dhalai', 'Dhalai'), ('North Tripura', 'North Tripura'), ('Pherzawl', 'Pherzawl'), ('Noney', 'Noney'), ('Ukhrul', 'Ukhrul'), ('Tengnoupal', 'Tengnoupal'), ('Thoubal', 'Thoubal'), ('Kangpokpi', 'Kangpokpi'), ('Jiribam', 'Jiribam'), ('Imphal East', 'Imphal East'), ('Churachandpur', 'Churachandpur'), ('Chandel', 'Chandel'), ('Bishnupur', 'Bishnupur'), ('Kakching', 'Kakching'), ('Imphal West', 'Imphal West'), ('Tamenglong', 'Tamenglong'), ('Senapati', 'Senapati'), ('Kamjong', 'Kamjong')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='nationality',
            field=models.CharField(blank=True, choices=[('India', 'India'), ('Unknown', 'Unknown'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua & Deps', 'Antigua & Deps'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia Herzegovina', 'Bosnia Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina', 'Burkina'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Central African Rep', 'Central African Rep'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Congo {Democratic Rep}', 'Congo {Democratic Rep}'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland {Republic}', 'Ireland {Republic}'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Ivory Coast', 'Ivory Coast'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea North', 'Korea North'), ('Korea South', 'Korea South'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Micronesia', 'Micronesia'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar, {Burma}', 'Myanmar, {Burma}'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('St Kitts & Nevis', 'St Kitts & Nevis'), ('St Lucia', 'St Lucia'), ('Saint Vincent & the Grenadines', 'Saint Vincent & the Grenadines'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City', 'Vatican City'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_from', models.DateTimeField(null=True)),
                ('time_to', models.DateTimeField(null=True)),
                ('address', models.TextField()),
                ('address_pt', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('type', models.CharField(blank=True, choices=[('placeVisit', 'placeVisit'), ('travel', 'travel')], max_length=15, null=True)),
                ('travel_mode', models.TextField()),
                ('place_name', models.TextField()),
                ('data_source', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
            ],
        ),
    ]
