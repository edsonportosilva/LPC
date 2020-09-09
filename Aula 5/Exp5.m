
% Experimento 5 - LPC
% C�digo auxiliar para ser utilizado na prepara��o do experimento.
%
%
% Autor: Edson Porto da Silva
%
% Descri��o: este c�digo tem a finalidade de servir como guia para
% modelagem da dispers�o crom�tica em um canal �ptico (fibra �ptica).
% Baseado neste c�digo o aluno dever� responder as quest�es da prepara��o
% bem como obter os coeficientes dos filtros FIR que ser�o utilizados no
% experimento computational no LPC.
%
% Obs.: Este c�digo � compat�vel com o MATLAB e OCTAVE.

clear
clc

% Par�metros da simula��o:
fa  = 128e3;    % frequ�ncia de amostragem (samp_rate)
sps = 16;       % n�mero de amostras por s�mbolo
fs  = fa/16;    % frequ�ncia de sinaliza��o (frequ�ncia de s�mbolos)
Ts  = 1/fs;     % per�odo de sinaliza��o (per�odo de s�mbolos)
Ntaps = 256;    % n�mero de coeficientes dos filtros FIR projetados

% Par�metros da fibra:
D      = 17e-6;                      % coeficiente de dispers�o crom�tica da fibra (s/m^2)
lambda = 1550e-9;                    % comprimento de onda da portadora(m)
c      = 3e5;                        % velocidade da luz no v�cuo (km/s)
L      = 1500;                       % dist�ncia de propaga��o do sinal (km)
beta2  = D*lambda^2/(2*pi*c);        % par�metro de dispers�o crom�tica de segunda ordem da fibra

omega  = 2*pi*linspace(-1/2,1/2, Ntaps)*(fa/16)*1e6; % vetor de frequ�ncias do sinal (escalonado para GHz para efeito did�tico)

% Resposta em frequ�ncia da dispers�o crom�tica:         
Hcd     = exp(1i*(beta2/2)*L*omega.^2);
% Resposta ao impulso (truncada) da dispers�o crom�tica:
hcd_fir = ifftshift(ifft(Hcd));

% Resposta em frequ�ncia do equalizador zero-forcing:
Hcd_zf     = 1./Hcd;
% Resposta ao impulso (truncada) do equalizador zero-forcing:
hcd_zf_fir = ifftshift(ifft(Hcd_zf));

close all
subplot(1,2,1),plot(abs(hcd_fir),'-*')
hold on,       plot(abs(hcd_zf_fir),'-o')
xlim([1 Ntaps])
title('Valor absoluto da resposta ao impulso')
legend('Canal','Equalizador ZF')
grid on;
subplot(1,2,2),plot(unwrap(angle(hcd_fir)),'-*')
hold on,       plot(unwrap(angle(hcd_zf_fir)),'-o')
xlim([1 Ntaps])
title('Fase da resposta ao impulso')
legend('Canal','Equalizador ZF')
grid on;

% Salva um arquivo .txt com os coefficientes dos filtros FIR no formato 
% requerido pelo GRC:

% Obs: os coeficientes gerados abaixo podem ser exportados para um filtro
% FIR no GRC apenas utilizando ctrl+c, ctrl+v.

filename = ['Exp5_L=' num2str(L) 'km.txt'];
fileID = fopen(filename,'w');

fprintf(fileID,'\n\nCoeficientes do filtro de dispers�o crom�tica para %d km:\n\n', L);
fprintf(fileID,'[');
for ii = 1:length(omega) 
    if ii ~= length(omega)
        if imag(hcd_fir(ii)) >= 0
            fprintf(fileID, '%.6f+%.6fj, ',real(hcd_fir(ii)), abs(imag(hcd_fir(ii))));
        else
            fprintf(fileID, '%.6f-%.6fj, ',real(hcd_fir(ii)), abs(imag(hcd_fir(ii))));
        end
    else
        if imag(hcd_fir(ii)) >= 0
            fprintf(fileID, '%.6f+%.6fj]',real(hcd_fir(ii)), abs(imag(hcd_fir(ii))));
        else
            fprintf(fileID, '%.6f-%.6fj]',real(hcd_fir(ii)), abs(imag(hcd_fir(ii))));
        end
    end
end

fprintf(fileID, '\n\n');
fprintf(fileID, '\n\nCoeficientes do filtro de equalizador zero-forcing para %d km:\n\n', L);
fprintf(fileID, '[');
for ii = 1:length(omega) 
    if ii ~= length(omega)
        if imag(hcd_zf_fir(ii)) >= 0
            fprintf(fileID, '%.6f+%.6fj, ',real(hcd_zf_fir(ii)), abs(imag(hcd_zf_fir(ii))));
        else
            fprintf(fileID, '%.6f-%.6fj, ',real(hcd_zf_fir(ii)), abs(imag(hcd_zf_fir(ii))));
        end
    else
        if imag(hcd_zf_fir(ii)) >= 0
            fprintf(fileID, '%.6f+%.6fj]',real(hcd_zf_fir(ii)), abs(imag(hcd_zf_fir(ii))));
        else
            fprintf(fileID, '%.6f-%.6fj]',real(hcd_zf_fir(ii)), abs(imag(hcd_zf_fir(ii))));
        end
    end
end
fprintf(fileID, '\n');
fclose(fileID);