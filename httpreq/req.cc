#include <iostream>
#include <curl/curl.h>

int main() {
    try{
    CURL* curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if (curl) {
        std::string url;
        std::cout << "Enter the URL: ";
        std::getline(std::cin, url);

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            std::cerr << "cURL request failed: " << curl_easy_strerror(res) << std::endl;
        }
        else {
            long response_code;
            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);
            std::cout << "Status code: " << response_code << std::endl;
        }

        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();

    return 0;}
    catch(const std::exception&e){
        std::cerr << e.what() << '\n';
    }
}