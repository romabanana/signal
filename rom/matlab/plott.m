function plott(type, domain, y)
  switch type
    case 0
      % Subplot %
      subplot(2,1,1);
      grid on;
      hold on;
      axis([0 1 -5 5]);
      title("Señal Original");
      stem(domain,y(1,:));
      subplot(2,1,2);
      hold on;
      grid on;
      axis([0 1 -5 5]);
      title("Señal Modificada");
      stem(domain,y(2,:));
    case 1
      % Overlay plot%
      grid on;
      hold on;
      axis([0 1 -5 5]);
      stem(domain, y(1,:), 'DisplayName', 'Señal Original');
      stem(domain, y(2,:), 'DisplayName', 'Señal Modificada');

      legend('show');
      legend('Location', 'northeast');


  endswitch
end
